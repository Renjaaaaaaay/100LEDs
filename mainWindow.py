from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setGeometry(50, 50, 200, 200)

    window.show()   #main application shows
    sys.exit(app.exec())    #to ensure clean exit of the program

window()
