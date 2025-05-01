from PyQt5.QtWidgets import QApplication
from qt_material import apply_stylesheet 
from interface.interface import MainWindow
import sys
import cProfile

def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    apply_stylesheet(app, theme='dark_blue.xml', invert_secondary=False, css_file='interface\\custom.css')
    window.show()

    app.exec()

if __name__ == "__main__":
    #cProfile.run('main()')
    main()
