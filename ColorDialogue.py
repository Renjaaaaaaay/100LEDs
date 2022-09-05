from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QColor
from pyqt_color_picker import ColorPickerWidget


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()


    def __initUi(self):
       
        defaultColor = QColor(255, 255, 255)
        colorPicker = ColorPickerWidget(color=defaultColor, orientation='vertical')
        
        colorPicker.colorChanged.connect(self.colorChanged)
    
        
        self.currentColor = QLabel()
      
        self.currentColor.setText(str(defaultColor))

        setColor_specificID = QPushButton('Set Color', self)
        setColor_toAll = QPushButton('Set Color to All', self)
        setColor_random = QPushButton('Set Random Animation', self)
        setColor_random.adjustSize()

        led_ID = QLabel('LED ID:', self)
        all_LED = QLabel('Set Color to All', self)

        lay = QVBoxLayout()
        lay.addWidget(setColor_specificID)
        lay.addWidget(setColor_toAll)
        lay.addWidget(setColor_random)
        lay.addWidget(led_ID)
        lay.addWidget(all_LED)
        lay.addWidget(colorPicker)
        lay.addWidget(self.currentColor)

        
        mainWidget = QWidget()
        mainWidget.setLayout(lay)
        self.setCentralWidget(mainWidget)
    
    def colorChanged(self, color):
         self.currentColor.setText(str(color))


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())