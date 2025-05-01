import librosa
import numpy as np

"""
Defines Audio_Graph: a handles that plots either a full-resolution step plot
or a reduced "envelope" view of an audio signal, depending on the current
zoom level. This method is inspired from matplotlib's displaywaveform.
"""

class Audio_Graph():
    """
    Dynamic audio waveform plotter with automatic downsampling

    Depending on current view span, it either:
    - draws every sample as a step plot (when zoomed in)
    - shows only the per-fram max/min envelope (when zoomed out)

    Attributes:
        graph       : A pyqtgraph PlotWidget to render into
        step_line   : PlotDataItem used for full-resolution waveform
        top_env_line    : PlotDataItem for positive envelope
        bottom_env_line : PlotDataItem for negative envelope
        y           : latest audio signal
        times       : time axis values corresponding to y
    """
    def __init__(self, graph, top_env, bottom_env):
        """
        use pre-created plot items and initialise internal state

        Args:
            graph   : PlotWidget where lines will be drawn
            top_env : PlotDataItem for the upper (positive) envelope
            bottom_env  : PlotDataItem for the lower (negative envelope)
        """
        self.graph = graph
        # step plot for high-resolution display
        self.step_line = graph.plot([0],[], stepMode=True)
        # pre-created envelope lines
        self.top_env_line = top_env
        self.bottom_env_line = bottom_env
        self.y = [] # buffer for most recent audio signal
        self.times = [] # corresponding time axis
    
    def getData(self, y, sr=22050):
        """
        Use new audio signal to update the display.
        Compute the time axis, choose step vs envelope mode
        and redraw appropriate PlotDataItem

        Args:
            y   : 1D (or 2D) Numpy array of audio signal
            sr  : sample rate used to compute timestamps
        """

        if len(y) == 0:
            # clear both envelopes if there's no data
            self.bottom_env_line.setData([],[])
            self.top_env_line.setData([],[])
            return
        
        # ensure we have 2D buffer
        if y.ndim == 1:
            y = y[np.newaxis, :]
        # build time axis for every frame
        self.times = librosa.core.times_like(y, sr=sr, hop_length=1)
        self._update_plot(y, sr)
        self.y = y
    
    def _update_plot(self, y, sr):
        """
        decide which view to show and recompute downsampling

        Args:
            y   : 2D array
            sr  : sample rate
        """
        #reduce by envelope calculation
        # hop ensures envelope has at most max_points values
        max_points = 11025
        hop = max(1, y.shape[-1]//max_points)
        x_frame = np.abs(librosa.util.frame(y, frame_length=hop, hop_length=hop))
        y_env = x_frame.max(axis=1)

        #split envelope into top and bottom
        y_bottom, y_top = -y_env[-1], y_env[0]

        #only plot up to max_points worth of data here
        xdata, ydata = self.times[:max_points], y[0, :max_points]
        envelope = [self.times[: len(y_top)* hop : hop], y_bottom, y_top]
        steps = [xdata, ydata[1:]]

        samples = y[0]
        view_lim = self.graph.getViewBox().viewRange()
        start, end = view_lim[0][0], view_lim[0][1]
        dim = (end - start) * sr
        xdata, ydata = self.times, samples

        # if viewport covers fewer than max_points samples use step mode
        data = steps[0]
        if dim <= max_points:
            if start <= data[0] or end >= data[-1]:
                # viewport expands beyond current data in steps; update
                # want to cover window of max_points centered on the current viewport
                midpoint_time = (start + end)/2
                idx_start = np.searchsorted(self.times, midpoint_time - 0.5 * max_points / sr)
                steps = [xdata[idx_start : idx_start + max_points],
                            ydata[idx_start : idx_start + max_points]]
            if len(steps[0]) == len(steps[1]):
                steps[0] = np.concatenate([steps[0], steps[0][-1:]])
            self.step_line.setData(steps[0], steps[1])
            self.step_line.setVisible(True)
            self.top_env_line.setVisible(False)
            self.bottom_env_line.setVisible(False)
        else:
            # envelope mode - plot one point per frame
            self.step_line.setVisible(False)
            self.top_env_line.setData(envelope[0], envelope[2])
            self.top_env_line.setVisible(True)
            self.bottom_env_line.setData(envelope[0], envelope[1])
            self.bottom_env_line.setVisible(True)
        

"""#test = Audio_Graph()
y, sr = librosa.load("C:/Users/uno4e/OneDrive/Documents/Cambridge II/project/music/sax_ehrling.mp3")
time = np.linspace(0, len(y)//sr, len(y))
plot(time, y, sr=sr)"""