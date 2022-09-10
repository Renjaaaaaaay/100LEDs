# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/Files/Code/repos/pyqt-colorpicker-widget/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("QLabel{\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #202020;")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_panel = QtWidgets.QFrame(self.centralwidget)
        self.left_panel.setStyleSheet("QFrame{\n"
"    background-color: #303030;\n"
"    border-radius: 10px;\n"
"}")
        self.left_panel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_panel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_panel.setObjectName("left_panel")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.left_panel)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.left_panel)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.left_content = QtWidgets.QFrame(self.left_panel)
        self.left_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_content.setObjectName("left_content")
        self.info = QtWidgets.QTextEdit(self.left_content)
        self.info.setGeometry(QtCore.QRect(10, 40, 341, 211))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.info.setFont(font)
        self.info.setStyleSheet("color: rgb(255, 255, 255);")
        self.info.setReadOnly(True)
        self.info.setObjectName("info")
        self.upd_lbl = QtWidgets.QLabel(self.left_content)
        self.upd_lbl.setGeometry(QtCore.QRect(90, 350, 201, 16))
        self.upd_lbl.setObjectName("upd_lbl")
        self.hex_label = QtWidgets.QLabel(self.left_content)
        self.hex_label.setGeometry(QtCore.QRect(110, 380, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(25)
        self.hex_label.setFont(font)
        self.hex_label.setObjectName("hex_label")
        self.verticalLayout_2.addWidget(self.left_content)
        self.horizontalLayout.addWidget(self.left_panel)
        self.right_panel = QtWidgets.QFrame(self.centralwidget)
        self.right_panel.setStyleSheet("QFrame{\n"
"    background-color: #303030;\n"
"    border-radius: 10px;\n"
"}")
        self.right_panel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right_panel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_panel.setObjectName("right_panel")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.right_panel)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.right_panel)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.colorpicker_area = QtWidgets.QFrame(self.right_panel)
        self.colorpicker_area.setMaximumSize(QtCore.QSize(16777215, 220))
        self.colorpicker_area.setStyleSheet("background-color: #222;")
        self.colorpicker_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.colorpicker_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.colorpicker_area.setObjectName("colorpicker_area")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.colorpicker_area)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.colorpicker_frame = QtWidgets.QFrame(self.colorpicker_area)
        self.colorpicker_frame.setMinimumSize(QtCore.QSize(360, 200))
        self.colorpicker_frame.setMaximumSize(QtCore.QSize(360, 200))
        self.colorpicker_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.colorpicker_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.colorpicker_frame.setObjectName("colorpicker_frame")
        self.horizontalLayout_2.addWidget(self.colorpicker_frame)
        self.verticalLayout.addWidget(self.colorpicker_area)
        self.pushButton = QtWidgets.QPushButton(self.right_panel)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: none;\n"
"    color: #fff;\n"
"    border: 4px solid #aaa;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #aaa;\n"
"    border: 4px solid #aaa;\n"
"    color: #000;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #666;\n"
"    color: #000;\n"
"    border: 4px solid #666;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.picked_color_lbl = QtWidgets.QLabel(self.right_panel)
        self.picked_color_lbl.setStyleSheet("")
        self.picked_color_lbl.setObjectName("picked_color_lbl")
        self.verticalLayout.addWidget(self.picked_color_lbl)
        self.selected_color_frame = QtWidgets.QFrame(self.right_panel)
        self.selected_color_frame.setMinimumSize(QtCore.QSize(0, 100))
        self.selected_color_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.selected_color_frame.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.selected_color_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.selected_color_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.selected_color_frame.setObjectName("selected_color_frame")
        self.verticalLayout.addWidget(self.selected_color_frame)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.right_panel, 0, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actiontest = QtWidgets.QAction(MainWindow)
        self.actiontest.setObjectName("actiontest")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "This is my custom App"))
        self.info.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Important for the colorpicker is the &quot;</span><span style=\" font-family:\'MS Shell Dlg 2\'; color:#279f0b;\">colorpicker_frame</span><span style=\" font-family:\'MS Shell Dlg 2\';\">&quot;.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">It serves as a </span><span style=\" font-family:\'MS Shell Dlg 2\'; color:#299f05;\">placeholder</span><span style=\" font-family:\'MS Shell Dlg 2\';\">, to which we will add the colorpicker widget programmatically, so be sure to know it\'s object name.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Open colorpicker\'s .ui file (colorpicker/ui_main.ui) to see how it is build.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Be sure to make the placeholder </span><span style=\" font-family:\'MS Shell Dlg 2\'; color:#289f0b;\">exactly 360x200 pixels</span><span style=\" font-family:\'MS Shell Dlg 2\';\">, as this is the size of the colorpicker, and it does not stretch/squash.</span></p></body></html>"))
        self.upd_lbl.setText(_translate("MainWindow", "LiveUpdate using colorChanged signal:"))
        self.hex_label.setText(_translate("MainWindow", "#000000"))
        self.label_2.setText(_translate("MainWindow", "Pick a Color here"))
        self.pushButton.setText(_translate("MainWindow", "Select Color"))
        self.picked_color_lbl.setText(_translate("MainWindow", "  Picked Color:"))
        self.actiontest.setText(_translate("MainWindow", "test"))
