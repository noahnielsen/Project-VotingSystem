# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(200, 200)
        MainWindow.setMinimumSize(QtCore.QSize(200, 200))
        MainWindow.setMaximumSize(QtCore.QSize(200, 200))
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radio_jane = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radio_jane.setGeometry(QtCore.QRect(110, 60, 51, 31))
        self.radio_jane.setObjectName("radio_jane")
        self.radio_john = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radio_john.setGeometry(QtCore.QRect(50, 60, 51, 31))
        self.radio_john.setObjectName("radio_john")
        self.button_submit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_submit.setGeometry(QtCore.QRect(60, 90, 81, 31))
        self.button_submit.setObjectName("button_submit")
        self.button_check = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_check.setGeometry(QtCore.QRect(120, 30, 75, 23))
        self.button_check.setObjectName("button_check")
        self.user_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.user_input.setGeometry(QtCore.QRect(10, 30, 101, 21))
        self.user_input.setObjectName("user_input")
        self.Label_main = QtWidgets.QLabel(parent=self.centralwidget)
        self.Label_main.setGeometry(QtCore.QRect(60, 0, 81, 21))
        self.Label_main.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Label_main.setObjectName("Label_main")
        self.label_error_message = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_error_message.setGeometry(QtCore.QRect(10, 130, 181, 31))
        self.label_error_message.setText("")
        self.label_error_message.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_error_message.setObjectName("label_error_message")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vote Menu"))
        self.radio_jane.setText(_translate("MainWindow", "Jane"))
        self.radio_john.setText(_translate("MainWindow", "John"))
        self.button_submit.setText(_translate("MainWindow", "Submit"))
        self.button_check.setText(_translate("MainWindow", "Check"))
        self.Label_main.setText(_translate("MainWindow", "ID Number"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
