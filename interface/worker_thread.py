from PyQt5.QtCore import *
from PyQt5.QtGui import *

import traceback, sys

class WorkerThreads(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(object)
    result = pyqtSignal(object)
    error = pyqtSignal(tuple)

class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerThreads()

        self.kwargs['progress_callback'] = self.signals.progress
    
    @pyqtSlot()
    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()
