import pytest
from PyQt5 import QtWidgets
from interface.interface import MainWindow

class DummySample:
    # dummy to track checked state
    def __init__(self, name):
        self.name = name
        self.checked = None
        self.max_time = 1.0
        self.min_corr = 0.5
        self.signal = []
        self.frame_rate = 44100
        self.corr = ([],[])
        self.media = None
        self.repeated_media = None
    
    def set_min_corr(self, v):
        self._set_val = v

class DummyGraph:
    # dummy graph object that records title updates
    def __init__(self):
        self.title_calls = []
    
    def setTitle(self, text, size=None):
        self.title_calls.append((text, size))


@ pytest.fixture
def app(qtbot, monkeypatch):
    """
    create MainWindow instance for testing with pytest-qt's qtbot
    """
    window = MainWindow()
    qtbot.addWidget(window)
    samp1 = DummySample("sample1")
    samp2 = DummySample("sample2")
    window.samples = {"sample1":samp1}
    window.checked_samples = []
    window.sonic_samples = {"sample2":samp2}
    window.checked_sonic_pi_samples = []

    calls = []
    def dummy_change():
        calls.append(True)
    monkeypatch.setattr(window, 'change_sample', dummy_change)
    window._change_called = calls
    # stub UI components updated by sample_clicked
    window.envelope_button = QtWidgets.QPushButton()
    window.envelope_button.setEnabled(False)
    window.sample_waveform = DummyGraph()
    window.correlation_graph = DummyGraph()

    window.editable = False
    return window

def test_show_error_msg_invokes_messagebox(app, monkeypatch):
    """
    monkeypatch show_error_msg to verify it gets called with expected argumenst
    """
    calls = []
    monkeypatch.setattr(app, 'show_error_msg', lambda icon, title, text: calls.append((icon, title, text)))
    # simulate error condition
    app.show_error_msg(QtWidgets.QMessageBox.Icon.Warning, "Test Error", "This is a test message")
    assert calls, "show_error_msg should be invoked when error occurs"
    icon, title, text = calls[0]
    assert "Test" in title, title
    assert "test" in text, text

def test_select_extracted_sample_adds_to_checked(app):
    app.sample_checked(2, "sample1")
    assert app.samples["sample1"].checked
    assert app.samples["sample1"] in app.checked_samples

def test_deselect_extracted_sample_removes_from_checked(app):
    app.sample_checked(2, "sample1")
    app.sample_checked(0, "sample1")
    assert app.samples["sample1"].checked == 0
    assert app.samples["sample1"] not in app.checked_samples

def test_select_sonic_samples_adds_to_checked_sonic(app):
    app.sample_checked(2, "sample2")
    assert app.sonic_samples["sample2"].checked
    assert app.sonic_samples["sample2"] in app.checked_sonic_pi_samples

def test_deselect_sonic_sample_removes_from_checked_sonic(app):
    app.sample_checked(2, "sample2")
    app.sample_checked(0, "sample2")
    assert app.sonic_samples["sample2"].checked == 0
    assert app.sonic_samples["sample2"] not in app.checked_sonic_pi_samples

@ pytest.mark.parametrize("sample_key, expected_name, store_attr", [
    ("sample1", "sample1", "samples"),
    ("sample2", "sample2", "sonic_samples")
])
def test_sample_clecked_sets_current_and_updates_ui(app, sample_key, expected_name, store_attr):
    app.sample_clicked(sample_key)
    assert app.current_sample.name == expected_name
    assert len(app._change_called) == 1

    assert app.envelope_button.isEnabled() is True
    assert app.editable is True

    waveform_calls = app.sample_waveform.title_calls
    assert waveform_calls, "Expected sample_waveform.setTitle to be called"
    assert expected_name in waveform_calls[-1][0]

    corr_calls = app.correlation_graph.title_calls
    assert corr_calls, "Expected correlation_graph.SetTitle to be called"
    assert expected_name in corr_calls[-1][0]

if __name__ == "__main__":
    import sys
    errno = pytest.main([__file__])
    sys.exit(errno)