from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow,QLineEdit
import sys

class setLabelbyPushButton(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        QMainWindow.setWindowTitle(self, 'This is my first Python GUI')     # use to set window title of program
        QMainWindow.setWindowFlags(self, QtCore.Qt.WindowCloseButtonHint)   # use to disable maximize and minimize buttons
        
        self.buttonA = QtWidgets.QPushButton('Click me', self)
        self.buttonA.clicked.connect(self.clickCallback)    
        self.buttonA.move(100, 50)

        self.labelA = QtWidgets.QLabel("I'm a label. Push the button.", self)
        self.labelA.adjustSize()
        self.labelA.move(110, 100)
        
        self.textboxA = QLineEdit(self)
        self.textboxA.setText('this is a default message')
        self.textboxA.move(100, 0)
        self.textboxA.resize(100,40)

        self.setGeometry(100, 100, 300, 200)
    def clickCallback(self):


        textboxValue = self.textboxA.text()
        self.labelA.setText(textboxValue)
        self.labelA.adjustSize()

if __name__ == "__main__": # to start the file.
    app = QApplication([])
    test = setLabelbyPushButton()
    test.show()
    sys.exit( app.exec_() ) # to ensure a clean exit of the application when X button is clicked.

     
'''
    def window():
        app = QApplication(sys.argv)

        window = QMainWindow()
        window.setGeometry(50, 50, 500, 500)
        window.setWindowTitle('This is a trial GUI')

        labelA = QtWidgets.QLabel(window)

        labelA.setText('This is a label.')
        labelA.setGeometry(200,200,200,200)

        pushButton = QtWidgets.QPushButton(window)

        pushButton.setText('This is a push button')
        pushButton.setGeometry(50,50,120,50)

        pushButton.clicked.connect(onClick)     #sets the event when the button is clicked



        window.show()   #main application shows
        sys.exit(app.exec())    #to ensure clean exit of the program

    def onClick():

        print('The button is pushed')

    window() '''
