from PyQt5.QtCore import QThreadPool, Qt, QTimer
from PyQt5.QtWidgets import (
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QWidget,
    QListWidget,
    QComboBox,
    QApplication,
    QFileDialog,
    QCheckBox,
    QListWidgetItem,
    QScrollArea,
    QStyle,
    QSlider,
    QDoubleSpinBox,
    QSplashScreen,
    QInputDialog,
    QAbstractItemView,
    QMessageBox
)
from PyQt5.QtGui import QPixmap, QIcon
import os
from interface.worker_thread import Worker
import shutil
import pyqtgraph as pg
from audio_processing.audiofile_manager import Sample_File, Original_Track_File, Sonic_Sample_File
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import numpy as np
from synthesis.program_generator import LoopProgramGenerator, DSLProgramGenerator
from interface.draggable_item import DraggableItem
from loop_extractor import LoopExtractor
from interface.audio_graph import Audio_Graph
from storage.audio_database import ProjectDatabase
from pymongo import MongoClient
from storage.audio_recogniser import Audio_Recogniser
from interface.load_window import LoadWindow


"""
Defines MainWindow, the central GUI for the Music Sample Remixer app
- a project browser back by MongoDB
- sample and built-in sonic pi sample panels
- waveform and similarity displays using PyQtGraph
- QMediaPlayer instances for sample, track and repeated playback
- Background workers (via QThreadPool) for loop extraction and synthesis

MainWindow handles all user interactions:
loading/uploading projects, selecting samples, editing envelopes, 
adjusting min-correlation thresholds, generating Sonic Pi program
from chosen samples
"""

class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        """
        Initialise main application window and all components

        Sets up:
        - window properties (title, minimum/initial size)
        - thread pool for background tasks
        - MongoDB connection (with error dialog on failure)
        - audio recogniser and loop extractor
        - loading screen for long running jobs - uploading file and generating program
        - primary layout: projects panel, samples panel, right-hand display
        - waveform and correlation plots via PyQtGraph
        - QMediaPlayer instances for sample/track/repeat playbacl
        - playback toolbars (play/pause/stop, volume sliders, edit envelopes)

        Args:
            *args, **kwards :   passed to QMainWindow constructor
        """
        super(MainWindow, self).__init__(*args, **kwargs)

        # window setup
        self.setWindowTitle("Music sample remixer")
        self.setMinimumSize(1500,900)
        self.resize(2250, 1350)

        # threadpool for large operations that need to be run without blocking UI
        self.threadpool = QThreadPool()

        # state holders
        self.current_sample = None
        self.checked_samples = []
        self.checked_sonic_pi_samples = []

        # mongoDB connection
        try:
            self.client = MongoClient("localhost", 27017)
        except Exception as e:
            self.show_error_msg(QMessageBox.Icon.Critical, 
                                 "Database Error", 
                                 f"Cannot connect to MongoDB: \n{e}")
            self.client = None

        # audio processors
        self.audio_recogniser = Audio_Recogniser()
        self.loop_extractor = LoopExtractor([0,0,0])

        # build UI components
        self._create_splash_screen()
        self._create_main_layout()
        self._create_projects_panel()
        self._create_samples_panel()
        self._create_right_layout()

        # stretch factors control how space is divided
        self.main_layout.setStretchFactor(self.left_sections, 2)
        self.main_layout.setStretchFactor(self.right_layout, 5)
        self.left_sections.setStretchFactor(self.project_panel, 1)
        self.left_sections.setStretchFactor(self.left_panel, 4)

        # plot displays
        self._create_sample_graph_display()
        self._create_track_graph_display()
        self._create_correlation_graph_display()

        # audio player for currently selected sample
        self.audio_sample_player = QMediaPlayer()
        self.audio_sample_player.error.connect( 
            lambda e: self.show_error_msg(QMessageBox.Icon.Warning, "Playback Error", self.audio_sample_player.errorString())
            )
        self.audio_sample_player.setNotifyInterval(10)
        self.audio_sample_player.positionChanged.connect(self.update_sample_pos)

        # build sample player toolbar
        self._create_sample_player_toolbar()

        # audio player for original track
        self.audio_track_player = QMediaPlayer()
        self.audio_track_player.error.connect( 
            lambda e: self.show_error_msg(QMessageBox.Icon.Warning, "Playback Error", self.audio_track_player.errorString())
            )
        self.audio_track_player.setNotifyInterval(10)
        self.audio_track_player.positionChanged.connect(self.update_track_pos)

        # audio player for where in original track that sample will be played
        self.audio_repeat_sample_player = QMediaPlayer()
        self.audio_repeat_sample_player.error.connect( lambda e: self.show_error_msg(QMessageBox.Icon.Warning, "Playback Error", self.audio_repeat_sample_player.errorString()))
        self.audio_repeat_sample_player.setNotifyInterval(10)
        self.audio_repeat_sample_player.positionChanged.connect(self.update_corr_pos)

        # build track-player toolbar
        self._create_track_player_toolbar()

        # initialise project path
        self.original_track_path = None

        # finalise central widget
        #self.create_temp_ui()
        widget = QWidget()
        widget.setLayout(self.main_layout)
        self.setCentralWidget(widget)
    
    def _create_splash_screen(self):
        #loading screen for when track being uploaded
        #load_pic = QPixmap('Refresh_icon.png').scaled(self.minimumSize(), Qt.KeepAspectRatio)
        #self.splash_screen = QSplashScreen(load_pic, Qt.WindowStaysOnTopHint)
        #self.splash_screen.setWindowOpacity(0.9)
        self.splash_screen = None
    
    def _create_main_layout(self):
        #main layout has side panel for list of samples and then main section with sample graphs and audio players
        self.main_layout = QHBoxLayout()
        self.left_sections = QHBoxLayout()
        self.main_layout.addLayout(self.left_sections)
        self.project_panel = QVBoxLayout()
        self.left_sections.addLayout(self.project_panel)
        self.left_panel = QVBoxLayout()
        self.left_sections.addLayout(self.left_panel)
        self.sample_panel = QVBoxLayout()
        self.left_panel.addLayout(self.sample_panel)
        self.two_samples_lists = QHBoxLayout()
        self.sample_list = QGridLayout()
        self.sample_list.setAlignment(Qt.AlignTop)
        self.built_in_sample_list = QGridLayout()
        self.built_in_sample_list.setAlignment(Qt.AlignTop)
    
    def _create_projects_panel(self):
        """
        Build the left-hand Projects panel
        - header label "PROJECTS
        - QListWidget for browsing existing projects
        - "+ UPLOAD" button to add a new project
        """
        #list of projects
        self.project_list = QListWidget()

        self.projects_header = QLabel("PROJECTS")
        self.projects_header.setProperty('class', 'heading')
        try:
            if not(os.path.exists("uploaded_projects")):
                os.mkdir("uploaded_projects")
        except OSError as e:
            self.show_error_msg(QMessageBox.Icon.Critical, "Filesystem Error", f"Could not create project folder: \n{e}")
            print(e)
        
        self.projects = self.get_project_names()
        self.project_list.addItems(self.projects)
        self.current_project = ""
        self.current_database = None
        if len(self.projects) > 0:
            self.current_project_path = f"uploaded_projects/{self.projects[0]}"
            #self.current_project = self.projects[0]
        else:
            #self.current_project = ""
            self.current_project_path = "uploaded_projects"

        self.projects_header.setAlignment(Qt.AlignCenter)
        self.project_panel.addWidget(self.projects_header)
        self.project_panel.addWidget(self.project_list)
        self.project_list.itemClicked.connect(self.project_clicked)
        self.project_list.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel) 
        
        #button to upload a new track and generate its samples
        self.new_upload_button = QPushButton("+ UPLOAD")
        self.new_upload_button.clicked.connect(self.new_upload)
        self.project_panel.addWidget(self.new_upload_button)

    
    def _create_samples_panel(self):
        """
        Build the left-hand "Samples" panel
        - a header label "SAMPLES"
        - two scrollable grids: extracted samples and built-in Sonic Pi samples
        - a "GENERATE" button to synthesize final Sonic Pi program
        """
        #scroll area for list of samples
        self.scroll_samp = QScrollArea()
        wrapper_widget = QWidget()
        wrapper_widget.setLayout(self.sample_list)
        self.scroll_samp.setWidget(wrapper_widget)
        self.scroll_samp.setWidgetResizable(True)

        #scroll area for list of sonic pi built in samples
        self.scroll_built_in = QScrollArea()
        wrapper_widget2 = QWidget()
        wrapper_widget2.setLayout(self.built_in_sample_list)
        self.scroll_built_in.setWidget(wrapper_widget2)
        self.scroll_built_in.setWidgetResizable(True)

        # set format for samples header
        self.sample_header = QLabel("SAMPLES")
        self.sample_header.setProperty('class', 'heading')
        self.samples = {}
        self.sonic_samples = {}
        self.sample_header.setAlignment(Qt.AlignCenter)
        self.sample_panel.addWidget(self.sample_header)

        self.sample_panel.addLayout(self.two_samples_lists)
        self.two_samples_lists.addWidget(self.scroll_samp)
        self.two_samples_lists.addWidget(self.scroll_built_in)

        #button to generate a sonic pi program
        self.generate_button = QPushButton("GENERATE")
        self.generate_button.setEnabled(False)
        self.generate_button.clicked.connect(self.generate_program)
        self.sample_panel.addWidget(self.generate_button)
    
    def _create_right_layout(self):
        """
        Build the right-hand display area
        - Sample-player section (waveform + controls)
        - Track-player section (waveform + controls)
        - Correlation graph section 
        """
        # right side of screen shows sample and track waveform and similarity measure
        self.right_layout = QVBoxLayout()
        self.main_layout.addLayout(self.right_layout)
        self.sample_player = QVBoxLayout()
        self.right_layout.addLayout(self.sample_player)
        self.right_layout.setStretchFactor(self.sample_player, 2)
        self.track_player = QVBoxLayout()
        self.right_layout.addLayout(self.track_player)
        self.right_layout.setStretchFactor(self.track_player, 3)
        self.sample_toolbar = QHBoxLayout()
        self.sample_player.addLayout(self.sample_toolbar)
        self.track_toolbar = QHBoxLayout()
        self.track_player.addLayout(self.track_toolbar)
        self.track_graph_box = QHBoxLayout()
        self.track_player.addLayout(self.track_graph_box)
        self.corr_graph_box = QHBoxLayout()
        self.track_player.addLayout(self.corr_graph_box)

    def _create_sample_graph_display(self):
        """
        Initialise sample waveform display
        This contains:
        - pyqtgraph PlotWidget for sample waveform
        - Audio_Graph for downsampled graph display
        - A ScatterPlotItem for envelope edit handles
        - an InfinitLine to track playback position
        """
        #graph showing sample audio waveform and its envelope
        pg.setConfigOptions(antialias=True)
        self.sample_waveform = pg.PlotWidget()
        self.sample_player.addWidget(self.sample_waveform)
        top_env_line = self.sample_waveform.plot([],[], pen= pg.mkPen(255,255,255), fillLevel=0, fillBrush=pg.mkBrush(255, 255, 255))
        bottom_env_line = self.sample_waveform.plot([],[], pen= pg.mkPen(255,255,255), fillLevel=0, fillBrush=pg.mkBrush(255, 255, 255))
        self.sample_line = Audio_Graph(self.sample_waveform, top_env_line, bottom_env_line)
        self.sample_waveform.setDownsampling(ds=True)
        self.sample_waveform.setTitle("Sample Waveform", size="10pt")
        pen = pg.mkPen(color=(0,255,255))
        self.env_line = self.sample_waveform.plot([],[], pen=pen, symbol="o", symbolSize=15)
        self.env_points = []
        #line to track position in audio file being played
        self.sample_pos_line = pg.InfiniteLine(angle=90, movable = True, pen=pg.mkPen((255,0,0)), hoverPen=pg.mkPen(0,0,255))
        self.sample_waveform.addItem(self.sample_pos_line)
        self.sample_pos_line.setZValue(1)
        self.sample_pos_line.sigPositionChangeFinished.connect(self.update_sample_play)
    
    def _create_track_graph_display(self):
        """
        Initialise original track waveform display
        This contains:
        - pyqtgraph PlotWidget for track waveform
        - Audio_Graph for downsampled graph display
        - an InfinitLine to track playback position
        - volume slider
        """
        #graph of whole track's waveform
        self.track_waveform = pg.PlotWidget()
        self.track_graph_box.addWidget(self.track_waveform)
        top_env_line = self.track_waveform.plot([],[], pen= pg.mkPen(255,255,255), fillLevel=0, fillBrush=pg.mkBrush(255, 255, 255))
        bottom_env_line = self.track_waveform.plot([],[], pen= pg.mkPen(255,255,255), fillLevel=0, fillBrush=pg.mkBrush(255, 255, 255))
        self.track_line = Audio_Graph(self.track_waveform, top_env_line, bottom_env_line)
        self.track_waveform.setDownsampling(ds=True)
        self.track_waveform.setTitle("Original Track Waveform", size="10pt")
        #has its own volume control
        self.track_vol = QVBoxLayout()
        self.track_vol_slider = QSlider(Qt.Vertical)
        self.track_graph_box.addLayout(self.track_vol)
        self.track_vol.addWidget(self.track_vol_slider)
        self.track_vol.setContentsMargins(0,50,0,50)
        self.track_graph_box.setContentsMargins(0,5,0,5)
        self.track_vol_slider.setMaximum(100)
        self.track_vol_slider.setMinimum(0)
        self.track_vol_slider.setSingleStep(1)

        #line to show where in original track is being played
        self.track_pos_line = pg.InfiniteLine(angle=90, movable = True, pen=pg.mkPen((255,0,0)), hoverPen=pg.mkPen(0,0,255))
        self.track_waveform.addItem(self.track_pos_line)
        self.track_pos_line.sigDragged.connect(self.update_track_play)
    
    def _create_correlation_graph_display(self):
        """
        Initialise similarity measure graph showing how well 
        the current sample matches each point in the track
        This contains:
        - pyqtgraph PlotWidget for graph
        - an InfinitLine to track playback position
        - volume slider
        - a horizontal min-correlation threshold line
        - scatter points at allowed match locations
        """
        #graph to show correlation between sample and original track
        self.correlation_graph = pg.PlotWidget()
        self.correlation_graph.setYRange(-0.5, 0.5)
        self.corr_graph_box.addWidget(self.correlation_graph)
        top_env_line = self.correlation_graph.plot([],[], fillLevel=0, fillBrush=pg.mkBrush(255, 255, 255))
        bottom_env_line = self.correlation_graph.plot([],[], fillLevel=0, fillBrush=pg.mkBrush(255, 255, 255))
        self.corr_line = Audio_Graph(self.correlation_graph, top_env_line, bottom_env_line)
        self.correlation_graph.getPlotItem().sigRangeChanged.connect(self.update_corr_graph_dat)
        self.correlation_graph.setDownsampling(ds=True)
        self.correlation_graph.setTitle("Sample Correlation Graph", size="10pt")
        #has its own volume control
        self.corr_vol = QVBoxLayout()
        self.corr_graph_box.addLayout(self.corr_vol)
        self.corr_vol_slider = QSlider(Qt.Vertical)
        self.corr_vol_slider.setMaximum(100)
        self.corr_vol_slider.setMinimum(0)
        self.corr_vol_slider.setSingleStep(1)
        self.corr_vol.addWidget(self.corr_vol_slider)
        self.corr_vol.setContentsMargins(0,50,0,50)
        self.corr_graph_box.setContentsMargins(0,5,0,5)

        #line to show where in original track is being played
        self.corr_pos_line = pg.InfiniteLine(angle = 90, movable = True, pen=pg.mkPen((255,0,0)), hoverPen=pg.mkPen(0,0,255))
        self.correlation_graph.addItem(self.corr_pos_line)
        self.corr_pos_line.sigDragged.connect(self.update_track_play)

        #line of the minimum correlation required for the sample to played at a location in the original track
        self.min_corr_line = pg.InfiniteLine(angle=0, movable = True, pen=pg.mkPen(0,255,0), hoverPen=pg.mkPen(0,0,255))
        #self.min_corr_line.sigDragged.connect(self.min_corr_dragged)
        self.min_corr_line.sigPositionChangeFinished.connect(self.min_corr_dragged)
        self.correlation_graph.addItem(self.min_corr_line)
        self.corr_intersection_points = pg.ScatterPlotItem(size=10, brush=pg.mkBrush(30, 255, 35, 255))
        self.correlation_graph.addItem(self.corr_intersection_points)
    
    def _create_sample_player_toolbar(self):
        """
        Build the playback toolbar for the selected sample
        This contains:
        - play / pause / stop buttons
        - volume slider
        - "Edit Envelope" button
        """
        #toolbar has play, pause, stop, volume control, edit envelope button
        self.play_sample_button = QPushButton()
        self.pause_sample_button = QPushButton()
        self.stop_sample_button = QPushButton()
        self.play_sample_button.setIcon(QIcon(self.style().standardIcon(QStyle.SP_MediaPlay)))
        self.pause_sample_button.setIcon(QIcon(self.style().standardIcon(QStyle.SP_MediaPause)))
        self.stop_sample_button.setIcon(QIcon(self.style().standardIcon(QStyle.SP_MediaStop)))
        self.play_sample_button.clicked.connect(self.audio_sample_player.play)
        self.pause_sample_button.clicked.connect(self.audio_sample_player.pause)
        self.stop_sample_button.clicked.connect(self.audio_sample_player.stop)

        for btn in (self.play_sample_button, self.pause_sample_button, self.stop_sample_button):
            btn.setEnabled(False)
            btn.setProperty('class', 'audioButton')
            self.sample_toolbar.addWidget(btn)
        self.sample_toolbar.addStretch()

        self.sample_volume_slider = QSlider(Qt.Horizontal)
        self.sample_volume_slider.setMaximum(100)
        self.sample_volume_slider.setValue(80)
        self.change_sample_volume(80)
        self.sample_volume_slider.setSingleStep(1)
        self.sample_volume_slider.valueChanged.connect(self.change_sample_volume)
        self.sample_toolbar.addWidget(self.sample_volume_slider)
        self.sample_toolbar.addStretch()

        self.envelope_button = QPushButton("EDIT ENVELOPE")
        self.envelope_button.setEnabled(False)
        #editing set to true if envelope being edited by user
        self.editing = False
        #editable set to true once a sample is clicked and loaded
        self.editable = False
        self.envelope_button.clicked.connect(self.edit_envelope)
        self.sample_toolbar.addWidget(self.envelope_button)
        self.sample_toolbar.addStretch()
    
    def _create_track_player_toolbar(self):
        """
        Build the playback toolbar for the original track and correlation
        This contains:
        - plat / pause / stop buttons (controls both track & repeat sample players)
        - min-correlation threshold spinbox
        """
        self.track_vol_slider.valueChanged.connect(self.audio_track_player.setVolume)
        self.track_vol_slider.setValue(50)

        #toolbar has play, pause, stop buttons and min correlation enter box
        self.play_track_button = QPushButton()
        self.play_track_button.setEnabled(False)
        self.pause_track_button = QPushButton()
        self.pause_track_button.setEnabled(False)
        self.stop_track_button = QPushButton()
        self.stop_track_button.setEnabled(False)
        self.play_track_button.setIcon(QIcon(self.style().standardIcon(QStyle.SP_MediaPlay)))
        self.pause_track_button.setIcon(QIcon(self.style().standardIcon(QStyle.SP_MediaPause)))
        self.stop_track_button.setIcon(QIcon(self.style().standardIcon(QStyle.SP_MediaStop)))
        self.play_track_button.setProperty('class', 'audioButton')
        self.pause_track_button.setProperty('class', 'audioButton')
        self.stop_track_button.setProperty('class', 'audioButton')
        #self.play_track_button.clicked.connect(self.play_track)
        self.play_track_button.clicked.connect(self.audio_track_player.play)
        #self.play_track_button.clicked.connect(self.play_large_track)
        self.pause_track_button.clicked.connect(self.audio_track_player.pause)
        #self.pause_track_button.clicked.connect(self.pause_large_track)
        self.stop_track_button.clicked.connect(self.audio_track_player.stop)
        self.track_toolbar.addWidget(self.play_track_button)
        self.track_toolbar.addWidget(self.pause_track_button)
        self.track_toolbar.addWidget(self.stop_track_button)
        self.track_toolbar.addStretch()

        self.corr_vol_slider.valueChanged.connect(self.audio_repeat_sample_player.setVolume)
        self.corr_vol_slider.setValue(80)

        #self.play_track_button.clicked.connect(self.play_corr)
        self.play_track_button.clicked.connect(self.audio_repeat_sample_player.play)
        self.pause_track_button.clicked.connect(self.audio_repeat_sample_player.pause)
        self.stop_track_button.clicked.connect(self.audio_repeat_sample_player.stop)

        self.min_corr_label = QLabel("MIN CORRELATION")
        self.min_corr_label.setProperty('class', 'littleHeading')
        self.min_corr_enter = QDoubleSpinBox()
        self.min_corr_enter.setMinimum(0.5)
        self.min_corr_enter.setDecimals(2)
        self.min_corr_enter.setEnabled(False)
        #self.min_corr_enter.editingFinished.connect(self.min_corr_val_change)
        self.min_corr_enter.valueChanged.connect(self.min_corr_val_change)
        self.track_toolbar.addWidget(self.min_corr_label)
        self.track_toolbar.addWidget(self.min_corr_enter)
        self.track_toolbar.addStretch()
    
    def show_error_msg(self, icon, title, text):
        QTimer.singleShot(0,lambda: 
            QMessageBox.critical(None, title, text)
        )
        """msg = QMessageBox()
        msg.setIcon(icon)
        msg.setWindowTitle(title)
        msg.setText(text)
        retval = msg.exec_()"""
    
    def update_sample_graph_dat(self):
        # update sample waveform
        if self.current_sample != None:
            self.sample_line.getData(self.current_sample.signal, self.current_sample.frame_rate)
    
    def update_track_graph_dat(self):
        # update track waveform
        if self.current_project != "":
            self.track_line.getData(self.original_track.signal, self.original_track.frame_rate)
    
    def update_corr_graph_dat(self):
        # update similarity measure
        if self.current_sample != None:
            self.corr_line.getData(self.current_sample.corr[1], self.original_track.frame_rate)
    
    def project_clicked(self, item):
        # reset checked samples
        self.checked_samples = []
        self.checked_sonic_pi_samples = []
        # triggered when user selects track
        self.current_project = item.text()
        self.current_project_path = f"uploaded_projects/{item.text()}"
        # update original track
        self.original_track_path = self.get_track()
        # find database
        self.current_database = ProjectDatabase(self.current_project)
        # update samples and clear current graphs
        self.current_sample = None
        self.sample_line.getData([])
        self.corr_line.getData([])
        self.corr_intersection_points.clear()
        self.audio_repeat_sample_player.setMedia(QMediaContent())
        self.set_original_track()
        self.set_sample_list()
        self.generate_button.setEnabled(True)

    def set_original_track(self, val=None):
        # change original track being worked with
        self.original_track = Original_Track_File("full_track", self.current_project, self.audio_recogniser, self.current_database)
        self.track_waveform.getPlotItem().sigRangeChanged.connect(self.update_track_graph_dat)
        self.correlation_graph.setXRange(0, self.original_track.max_time)
        self.update_waveform(self.original_track, self.track_line, "track")
        self.audio_track_player.setMedia(QMediaContent())
        self.audio_track_player.setMedia(self.original_track.media)
        self.play_track_button.setEnabled(True)
        self.pause_track_button.setEnabled(True)
        self.stop_track_button.setEnabled(True)
        self.min_corr_enter.setEnabled(True)
 
    def play_track_corr(self, progress_callback=None):
        # when bottom toolbar play button clicked simultaneously play 
        # original track and audio with where sample would be played in track
        self.audio_track_player.play()
        self.audio_repeat_sample_player.play()
    
    def play_large_track(self):
        # play the original track audios
        self.play_track_corr()
    
    def pause_track_corr(self, progress_callback=None):
        # when when bottom toolbar pause button clicked simultaneously pause 
        # original track and audio with where sample would be played in track
        self.audio_track_player.pause()
        self.audio_repeat_sample_player.pause()
    
    def pause_large_track(self):
        # pause the original track audios
        self.pause_track_corr()
    
    def get_project_names(self):
        #get names of uploaded projects
        try:
            if not self.client:
                return
            try:
                projects = self.client.list_database_names()
            except Exception as e:
                self.show_error_msg(QMessageBox.Icon.Warning, "DB Query Failed", str(e))
                return
            unwanted = ["admin", "config", "local", "SonicPiSamples"]
            for u in unwanted:
                projects.remove(u)
        except Exception as error:
            print("Error with getting uploaded projects:", error)
            return []
        return projects
    
    def get_track(self):
        # get name path to original track
        try:
            track = [name for name in os.listdir(f"{self.current_project_path}/full_track") if os.path.isfile(os.path.join(f"{self.current_project_path}/full_track", name))]
        except OSError as e:
            self.show_error_msg(QMessageBox.Icon.Critical, "Filesystem Error", f"could not get track file:\n{e}")
            print("error with getting track:", e)
            return None
        if len(track) > 0:
            path = f"{self.current_project_path}/full_track/{track[0]}"
            return path
        return None
    
    def get_samples(self, progress_callback=None):
        # get list of samples
        try:
            all_samples = self.current_database.get_sample_names()
            print(all_samples)
            for i, name in enumerate(all_samples):
                samp = Sample_File(file=name, 
                                   name=name,
                                   full_track=self.original_track, 
                                   database=self.current_database, 
                                   rank=0)
                self.samples[name] = samp
                if progress_callback != None:
                    progress_callback.emit((i, name, self.sample_list, True))
                else:
                    self.add_checkbox((i, name, self.sample_list, True))

            """for i, name in enumerate(os.listdir(f"{self.current_project_path}/samples")): 
                path = os.path.join(f"{self.current_project_path}/samples", name)
                if os.path.isfile(path):
                    self.samples[name] = Sample_File(f"{self.current_project_path}/samples/{name}", name, self.original_track, self.current_database)
                    if progress_callback != None:
                        progress_callback.emit((i, name, self.sample_list, True))
                    else:
                        self.add_checkbox((i, name, self.sample_list, True))
            """        
        except Exception as e:
            self.show_error_msg(QMessageBox.Icon.Critical, "Filesystem Error", f"Could not get sample names: \n{e}")
            print("Error with getting sample names:", e)
    
    def get_sonic_pi_samples(self, progress_callback=None):
        try:
            # order sonic pi samples by how similar how many similarities were found to original
            ordered_sonic_samples = self.current_database.get_order_sonic_pi_samples()
            print(ordered_sonic_samples)
            for i, song in enumerate(ordered_sonic_samples):
                self.sonic_samples[song] = Sonic_Sample_File(f"sample-pi-main/{song}", song, self.original_track, self.current_database, i)
                if progress_callback != None:
                    progress_callback.emit((i,song, self.built_in_sample_list, False))
                else:
                    self.add_checkbox((i,song, self.built_in_sample_list, False))
        except OSError as error:
            print("Error with getting sonic pi samples:", error)
    
    def add_checkbox(self, args):
        i, name, grid, state = args
        # put a checkbox and button for a sample
        # checkbox to include sample in final output
        # button to select and manipulate particular sample
        check_box = QCheckBox()
        check_box.stateChanged.connect(lambda state, x=name: self.sample_checked(state, x))
        check_box.setChecked(state)
        grid.addWidget(check_box, i, 0)
        sample_button = QPushButton(name)
        sample_button.setCheckable(True)
        sample_button.setProperty('class', 'listButton')
        sample_button.clicked.connect(lambda _, x=name: self.sample_clicked(x))
        sample_button.clicked.connect(lambda _, x=sample_button: self.clicked_button_colour(x))
        grid.addWidget(sample_button, i, 1)
    
    def clicked_button_colour(self, button):
        # selected sample turns different colour
        # first unhighlight all other buttons
        for i in reversed(range(self.sample_list.count())):
            if i%2 == 1:
                if self.sample_list.itemAt(i).widget().isChecked():
                    self.sample_list.itemAt(i).widget().setChecked(False)
        for i in reversed(range(self.built_in_sample_list.count())):
            if i%2 == 1:
                if self.built_in_sample_list.itemAt(i).widget().isChecked():
                    self.built_in_sample_list.itemAt(i).widget().setChecked(False)
        button.setChecked(True)

    def reset_sample_list(self, progress_callback=None):
        # clear any items that might already be in the list
        for i in reversed(range(self.sample_list.count())):
            self.sample_list.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.built_in_sample_list.count())):
            self.built_in_sample_list.itemAt(i).widget().setParent(None)
        # get current list of samples
        self.get_samples(progress_callback)
        self.get_sonic_pi_samples(progress_callback)
    
    def set_sample_list(self):
        """
        Spawn backgrown worker to load all samples (extracted and Sonic Pi)
        without blocking the UI, and update the checkbox grid as each
        one finishes loading

        Signals:
        - progress (index, name, layout, is_extracted_sample) -> add_checkbox
        - error (exception) -> critical dialog
        """
        # create thread to set up each loaded sample in the folder
        # samples will apear one by one as they are loaded
        worker = Worker(self.reset_sample_list)
        worker.signals.progress.connect(self.add_checkbox)
        worker.signals.error.connect(lambda e: self.show_error_msg(QMessageBox.Icon.Critical, "Background Task Failed", str(e)))
        self.threadpool.start(worker)
    
    def set_editable(self, val):
        self.editable = val
    
    def change_sample(self, progress_callback=None):
        # change current selected sample
        self.set_editable(False)
        # if user exited last sample without saving edited envelope, save it
        if self.editing:
            self.save_edit()
            self.editing = False
        # create thread to change sample audio waveform
        self.update_waveform(self.current_sample, self.sample_line, "sample")
        self.sample_waveform.getPlotItem().sigRangeChanged.connect(self.update_sample_graph_dat)
        self.correlation_graph.setXRange(0, self.current_sample.max_time)
        self.correlation_graph.setXRange(0, self.original_track.max_time)
        # create thread to change sample correlation graph
        self.update_correlation(self.current_sample, self.corr_line)
        
        # load min correlation for this sample
        # make sure offsets are updated even if min correlation is the same value as it was for the last sample
        if self.min_corr_enter.value() == self.current_sample.min_corr:
            self.min_corr_val_change(self.current_sample.min_corr)
        else:
            self.min_corr_enter.setValue(self.current_sample.min_corr)
        # change audio players to play current sample
        self.audio_sample_player.setMedia(QMediaContent())
        self.audio_sample_player.setMedia(self.current_sample.media)
        self.audio_repeat_sample_player.setMedia(QMediaContent())
        self.audio_repeat_sample_player.setMedia(self.current_sample.repeated_media)
        self.audio_track_player.setPosition(0)
        self.play_sample_button.setEnabled(True)
        self.pause_sample_button.setEnabled(True)
        self.stop_sample_button.setEnabled(True)
    
    def sample_clicked(self, sample):
        # triggered when a sample is clicked
        if sample in self.samples.keys():
            self.current_sample = self.samples[sample]
        else:
            self.current_sample = self.sonic_samples[sample]
        self.change_sample()
        # once the new sample has been loaded you can edit the envelope
        self.envelope_button.setEnabled(True)
        self.set_editable(True)
        self.sample_waveform.setTitle(f"{self.current_sample.name} waveform", size="10pt")
        self.correlation_graph.setTitle(f"{self.current_sample.name} correlation graph", size="10pt")
        
    def sample_checked(self, checked, sample):
        # triggered when a sample checkbox is clicked
        if sample in self.samples.keys():
            samp = self.samples[sample]
            samp.checked = checked
            if checked and samp not in self.checked_samples:
                self.checked_samples.append(samp)
            elif samp in self.checked_samples:
                self.checked_samples.remove(samp)
        else:
            samp = self.sonic_samples[sample]
            samp.checked = checked
            if checked and samp not in self.checked_sonic_pi_samples:
                self.checked_sonic_pi_samples.append(samp)
            elif samp in self.checked_sonic_pi_samples:
                self.checked_sonic_pi_samples.remove(samp)
    
    def update_waveform(self, audio, line, graph, progress_callback=None):
        # update the waveform of line to the waveform of audio
        # graph will be "sample" or "track" indicating which graph is being changed
        if graph == "sample":
            self.update_sample_graph_dat()
            env = audio.get_envelope()
            self.env_line.setData(env[0], env[1])
        else:
            self.update_track_graph_dat()

    def update_correlation(self, audio, line, progress_callback=None):
        # update the correlation graph
        self.update_corr_graph_dat()
        self.min_corr_enter.setMaximum(audio.max_corr + 1)
        max_y = np.max(line.y)
        self.correlation_graph.setYRange(-max_y, max_y)

    def change_sample_volume(self, vol):
        self.audio_sample_player.setVolume(vol)
    
    def change_track_volume(self, vol):
        self.audio_track_player.setVolume(vol)
        self.audio_repeat_sample_player.setVolume(vol)
    
    def find_play_x(self, pos, progress_callback=None):
        """
        Convert playback position in ms to non-negative seconds

        Args:
            pos_ms: Position from QMediaPlayer (milliseconds)
        Returns:
            float: position in seconds, never negative
        """
        # find x value for line that monitors position in an audio file
        pos = max(pos/1000, 0)
        return pos

    def find_v_line_x(self, pos, line):
        """
        covert x-coordinate from draggable InfiniteLine to data range

        Args:
            pos :   x position from the line (seconds)
            line :  AudioGraph instance holding times array
        Returns:
            float: clamped x within [min_time, max_time]
        """
        x_data = line.times
        x_min = np.min(x_data)
        x_max = np.max(x_data)
        # line can't be dragged beyond limits of audio file
        if pos < x_min:
            pos = x_min
        elif pos > x_max:
            pos = x_max
        return pos
    
    def update_sample_pos(self, pos):
        """
        Slot for QMediaPlayer.positionChanged: move the sample-playhead line
        converts the player's millisecond pos to seconds
        then sets InfiniteLine's x pos
        """
        pos = self.find_play_x(pos)
        self.sample_pos_line.setPos(pos)
    
    def play_sample_at_pos(self, pos):
        """
        Jump the sample player to a given time (seconds)
        Args:
            pos :   Target time in seconds
        """
        self.audio_sample_player.setPosition(int(pos*1000))
    
    def update_sample_play(self, v_line):
        """
        Slot for InfinitLine.sigPositionChangeFinished on the sample graph
        when the user drags the playhead, read its x and
        seek the audio accordingly
        """
        pos = self.find_v_line_x(v_line.pos()[0], self.sample_line)
        self.play_sample_at_pos(pos)
    
    def update_track_pos(self, pos):
        """
        Slot for QMediaPlayer.positionChanged: move the track playhead line
        Args:
            pos :   milliseconds from audio_track_player.positionChanged
        """
        x = self.find_play_x(pos)
        self.track_pos_line.setPos(x)
    
    def update_corr_pos(self, pos):
        """
        Slot for QMediaPlayer.positionChanged on the repeat-sample player
        keeps correlation graph's playhead in sync with the sample within the track player
        """
        x = self.find_play_x(pos)
        self.corr_pos_line.setPos(x)
        
    def play_track_at_pos(self, pos):
        """
        Jump both track and repeat-sample players to a specific time
        ensures they remain synchronised when seeking
        """
        milli_sec = int(pos * 1000)
        self.audio_track_player.setPosition(milli_sec)
        self.audio_repeat_sample_player.setPosition(milli_sec)
    
    def update_track_play(self, v_line):
        """
        Slot for dragging either track or correlation playhead
        when the user drags an InfiniteLine on either line, clamp and seek both players
        """
        pos = self.find_v_line_x(v_line.pos()[0], self.track_line)
        self.play_track_at_pos(pos)
    
    def change_min_corr(self):
        # update the minimum correlation for the current sample
        self.current_database.update_sample_data(self.current_sample)
        # update the intersection points on the graph
        self.corr_intersection_points.clear()
        self.corr_intersection_points.addPoints(self.current_sample.offsets, self.current_sample.val_arr)
        # update the audio content for where in the track the sample will be played
        self.audio_repeat_sample_player.setMedia(QMediaContent())
        self.audio_repeat_sample_player.setMedia(self.current_sample.repeated_media)
        # put track audio in same poistion as audio sample reoeat player
        self.audio_track_player.setPosition(0)
    
    def min_corr_val_change(self, val):
        """
        User changed the min-correlation spinbox
        recalculates valid offsets in the background and then 
        update the graph + audio playback
        Signals:
        - result(_) -> change_min_corr (redraws points & reloads media)
        - error (exception) -> critical dialog
        """
        # triggered when value in min correlation entry is changed
        # create thread to update offsets for where sample will be played in original track
        worker = Worker(self.current_sample.set_min_corr, val)
        worker.signals.result.connect(self.change_min_corr)
        worker.signals.error.connect(lambda e: self.show_error_msg(QMessageBox.Icon.Critical, "Background Task Failed", str(e)))
        self.threadpool.start(worker)
        # move min correlation line on graph if not in correct place
        if self.min_corr_line.pos()[1] != val:
            self.min_corr_line.setPos(val)
    
    def min_corr_dragged(self, h_line):
        # triggered when min correlation line is moved
        self.min_corr_enter.setValue(h_line.pos()[1])
    
    def edit(self):
        """
        Enter "edit envelope" mode: replace the static envelope line
        with draggable handles so the user can reshapes the ADSR points

        Creates 5 DraggableItem hangles at the current envelope coordinates:
        - Index 0: start point (fixed y=0)
        - Index 4: release point (fixed y=0)
        - Index 1-3: attack, decay, sustain (movable within [0, max_time] on x,
            and [0, max_vol] on y)
        """
        # change button text to finish editing
        self.envelope_button.setText("FINISH EDITING")
        env = self.env_line.getData()

        # make envelope points movable and set appropriate bounds for each of them
        self.env_points = []
        max_x = self.current_sample.max_time
        for i in range(5):
            if i == 0 or i == 4:
                y_bound = (0,0)
            else:
                y_bound = (0, self.current_sample.max_vol)
            
            target_point = DraggableItem(
                self.env_line, 
                i, 
                (env[0][i],env[1][i]), 
                pg.mkPen(0,255,255), 
                pg.mkPen(0,255,0), 
                (0, max_x), 
                y_bound)
            self.env_points.append(target_point)
            self.sample_waveform.addItem(target_point)

    def save_edit(self):
        """
        Exit "edit envelope" mode: remove draggable handles, enforce monotoni x,
        collect their final positions, update the sample's envelopes, and redraw
            - read each envelope point's pos, clamp to xs non-decreasing
            - remove the draggable item from the plot
            - call sample.set_env([xs, ys]) and update stored metadata
            - redraw static env_line with new coords
            - re-apply ADSR to audio and reload QMediaPlayer media
        """
        # triggered when finish editing clicked
        # change button text back to edit envelope
        self.envelope_button.setText("EDIT ENVELOPE")
        env_x = []
        env_y = []
        # remove movable points
        # update new envelope positions
        for i, p in enumerate(self.env_points):
            pos = p.pos()
            if i > 0:
                if pos[0] < self.env_points[i-1].pos()[0]:
                    pos[0] = self.env_points[i-1].pos()[0]
            env_x.append(min(self.current_sample.max_vol, pos[0]))
            env_y.append(max(0, pos[1]))
            self.sample_waveform.removeItem(p)

        self.current_sample.set_env_with_list([env_x, env_y])
        self.env_line.setData(env_x, env_y)
        self.current_database.update_sample_data(self.current_sample)
        # update sample audio to implement new envelope
        self.audio_sample_player.setMedia(QMediaContent())
        self.audio_sample_player.setMedia(self.current_sample.implement_envelope())
        # update repetition of sample audio to play it with enveloped samples
        self.audio_repeat_sample_player.setMedia(QMediaContent())
        self.audio_repeat_sample_player.setMedia(self.current_sample.repeated_media)
        # set position of original track back to zero so it stays consistent with correlation graph
        self.track_pos_line.setPos(0)
    
    def edit_envelope(self):
        """
        Toggle between editing mode and non editing mode when button clicked
        - if no sample loaded, do nothing
        - if not currently editing, call self.edit()
        - otherwise call self.save_edit() to finalise changes
        """
        # triggered when edit envelope/finish editing button clicked
        # nothing happens if sample not loaded yet
        if self.editable:
            self.editing = not(self.editing)
            if self.editing:
                self.edit()
            else:
                self.save_edit()
        
    def extract_loops(self, source_path, dest_path, dest_dir, progress_callback=None):
        # run algorithm to generate samples
        self.loop_extractor.run_algorithm(source_path, dest_path, dest_dir, self.current_database, progress_callback)
        self.splash_screen.close()
    
    def new_upload(self):
        """
        After the user picks a file and enters a project name,
        spawn a worker to extract loops on a separate thread
        Signals:
        - progress (full track data) -> set_original_track (updates the track display)
        - result (_) -> set_sample_list (populates samples panel)
        - error (excepion) -> critical dialog
        """
        # file dialog opens to select an audio file
        file_name = QFileDialog.getOpenFileName(self, "Select an Audio File")
        project_name, entered = QInputDialog.getText(self, 'Input Upload Name', 'Enter project title:')
        if not entered or not project_name.strip() or not file_name:
            self.show_error_msg(QMessageBox.Icon.Information, "Upload Cancelled", "You must a enter a project name to continue")
            return
        
        # disable access to main window by showing loading screen
        self.splash_screen = LoadWindow(self)
        self.splash_screen.show()
        # get full path and chunks of file path
        path = os.path.abspath(file_name[0])
        file_chunks = os.path.splitext(file_name[0])
        # check it is an wav or mp3 file
        if file_chunks[1] != ".wav" and file_chunks[1] != ".mp3":
            print("wrong file type")
        else:
            #create new project folder
            try:
                os.mkdir(f"uploaded_projects/{project_name}")
                self.current_project_path = f"uploaded_projects/{project_name}"
                self.current_project = project_name
                self.projects.append(project_name)
                self.project_list.addItem(project_name)
                os.mkdir(f"{self.current_project_path}/full_track")
                os.mkdir(f"{self.current_project_path}/samples")
                #os.mkdir(f"{self.current_project_path}/samples_full_vol")
                #os.mkdir(f"{self.current_project_path}/enveloped_samples")
                #os.mkdir(f"{self.current_project_path}/repeated_samples")
                #os.mkdir(f"{self.current_project_path}/sonic_pi_samples")
                #os.mkdir(f"{self.current_project_path}/loop_tracks")
                # copy in audio file to appropriate folder
                shutil.copy(path, f"{self.current_project_path}/full_track")
                track_name = os.listdir(f"{self.current_project_path}/full_track")[0]
                self.original_track_path = f"{self.current_project_path}/full_track/{track_name}"
                self.current_database = ProjectDatabase(project_name)

            except OSError as e:
                self.show_error_msg(QMessageBox.Icon.Critical, "Filesystem Error", f"could not make new project folder:\n{e}")
                print("error making new project folder:", e)
            except Exception as e:
                self.show_error_msg(QMessageBox.Icon.Critical, "Copy failed", f"Unable to copy to prohect folder:\n{e}")
            # create thread to extract new sample loops
            worker = Worker(self.extract_loops, path, f"{self.current_project_path}/samples/sample", self.current_project_path)
            worker.signals.result.connect(self.set_sample_list)
            worker.signals.progress.connect(self.set_original_track)
            worker.signals.error.connect(lambda e: self.show_error_msg(QMessageBox.Icon.Critical, "Background Task Failed", str(e)))
            self.threadpool.start(worker)

    def generate_program(self):
        """
        Trigger Sonic Pi program synthesis using currently checked samples
        method called when user clicks "GENERATE" button
        - gathers user-selected sample objects
        - instantiates program generator with those lists and the samples folder path
        - shows a loading screen while synthesis runs
        """
        #print(self.original_track.downbeats)
        #disable generate button to prevent re-entry
        #self.generate_button.setEnabled(False)

        #show loadng screen
        self.splash_screen = LoadWindow(self)
        self.splash_screen.show()

        # create thread to synthesise file
        worker = Worker(self.generate_file)
        worker.signals.error.connect(lambda e: self.show_error_msg(QMessageBox.Icon.Critical, "Background Task Failed", str(e)))
        self.threadpool.start(worker)
    
    def generate_file(self, progress_callback=None):
        #create generator
        program_generator = DSLProgramGenerator(
            self.checked_samples, 
            self.checked_sonic_pi_samples, 
            os.path.join(self.current_project_path, "samples")
            )
        # run algorithm to synthesise file
        try:
            program_generator.synthesise_file(self.current_project_path)
        except Exception as e:
            self.show_error_msg(QMessageBox.Icon.Critical, "Synthesis Error", f"Could not generate program:\n{e}")
        finally:
            self.splash_screen.close()
            #self.generate_button.setEnabled(True)
    
    def create_temp_ui(self):
        # temporary UI while it was being developed
        left_panel_pixmap = QPixmap("UI/left_panel.jpg")
        left_panel = QLabel()
        left_panel.setScaledContents(True)
        left_panel.setPixmap(left_panel_pixmap)
        self.left_panel.addWidget(left_panel)

        top_toolbar_pixmap = QPixmap("UI/top_toolbar.jpg")
        top_toolbar = QLabel()
        top_toolbar.setScaledContents(True)
        top_toolbar.setPixmap(top_toolbar_pixmap)
        self.sample_toolbar.addWidget(top_toolbar)

        sample_graph_pixmap = QPixmap("UI/sample_specto.jpg")
        sample_graph = QLabel()
        sample_graph.setScaledContents(True)
        sample_graph.setPixmap(sample_graph_pixmap)
        self.sample_player.addWidget(sample_graph)

        bottom_toolbar_pixmap = QPixmap("UI/bottom_toolbar.jpg")
        bottom_toolbar = QLabel()
        bottom_toolbar.setScaledContents(True)
        bottom_toolbar.setPixmap(bottom_toolbar_pixmap)
        self.track_toolbar.addWidget(bottom_toolbar)

        track_graph_pixmap = QPixmap("UI/track_specto.jpg")
        track_graph = QLabel()
        track_graph.setScaledContents(True)
        track_graph.setPixmap(track_graph_pixmap)
        self.track_player.addWidget(track_graph)

        correlation_pixmap = QPixmap("UI/sample_correlation.jpg")
        correlation_graph = QLabel()
        correlation_graph.setScaledContents(True)
        correlation_graph.setPixmap(correlation_pixmap)
        self.track_player.addWidget(correlation_graph)
    
    
