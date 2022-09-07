# This is a practice file on how to implement the grid layout to the GUI.

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QMainWindow

import sys

from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QColor
from pyqt_color_picker import ColorPickerWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()
    
 
    def __initUi(self):
        self.setWindowTitle("PyQt5 GridLayout")
        self.setWindowIcon(QIcon('python.png'))
       
        defaultColor = QColor(255, 255, 255)
        colorPicker = ColorPickerWidget(color=defaultColor, orientation='vertical')
        
        colorPicker.colorChanged.connect(self.colorChanged) # to connect when color changes
    
        
        self.currentColor = QLabel()
      

        setColor_specificID = QPushButton('Set Color', self)
        setColor_toAll = QPushButton('Set Color to All', self)
        setColor_random = QPushButton('Set Random Animation', self)
        setColor_random.adjustSize()

        led_ID = QLabel('LED ID:', self)
        all_LED = QLabel('Set Color to All', self)

        lay = QGridLayout()
        lay.addWidget(setColor_specificID, 0, 0)
        lay.addWidget(setColor_toAll, 0, 1)
        lay.addWidget(setColor_random, 0, 2)
        lay.addWidget(led_ID, 1, 0)
        lay.addWidget(all_LED, 1, 1)
        lay.addWidget(colorPicker, 1, 3)
        lay.addWidget(self.currentColor, 0, 4)

        
        self.setLayout(lay)
        
    
    def colorChanged(self, color):
         r = color.red()
         g = color.green()
         b = color.blue()

         self.currentColor.setText("Current color is " f'R{str(r)}, G{str(g)}, B{str(b)}') # TO DISPLAY RGB
               

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
