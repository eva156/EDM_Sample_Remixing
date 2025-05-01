from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
    QDialog
)
from PyQt5.QtGui import QMovie

"""
LoadWindow dialog displays a gif loading animation to 
block user interaction during long-running background tasks
"""

class LoadWindow(QDialog):
    """
    dialog showing an animated loading spinner
    blocks user interaction with parent window while GIF plays
    """
    def __init__(self, parent):
        """
        Initialise loading dialog
        Args:
            parent : QMainWindow that owns the dialog
        """
        super().__init__(parent)
        self.setWindowModality(Qt.WindowModal)
        self.setGeometry(0,0,500,500)
        self.setWindowTitle("Load Window")
        
        self.centralwidget = QWidget()
        
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(25,25,400,400))
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.movie = QMovie("interface\\loading.gif")
        self.label.setMovie(self.movie)
        # start animation immediately
        self.startAnimation()
    
    def startAnimation(self):
        # start or resume loading animation
        self.movie.start()
    
    def stopAnimation(self):
        # stop or pause loading animation
        self.movie.stop()
