from PyQt5 import QtWidgets, QtGui, QtCore
from calculate import Ui_MainWindow
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.i = 0
        self.ui.pushButton.clicked.connect(self.button7)
        self.ui.pushButton_2.clicked.connect(self.button8)
        self.ui.pushButton_3.clicked.connect(self.button9)
        self.ui.pushButton_4.clicked.connect(self.button_add)
        self.ui.pushButton_5.clicked.connect(self.button_Clear)
        self.ui.pushButton_6.clicked.connect(self.button4)
        self.ui.pushButton_7.clicked.connect(self.button5)
        self.ui.pushButton_8.clicked.connect(self.button6)
        self.ui.pushButton_9.clicked.connect(self.button_minus)
        self.ui.pushButton_10.clicked.connect(self.button1)
        self.ui.pushButton_11.clicked.connect(self.button2)
        self.ui.pushButton_12.clicked.connect(self.button3)
        self.ui.pushButton_13.clicked.connect(self.button_times)
        self.ui.pushButton_14.clicked.connect(self.button0)
        self.ui.pushButton_15.clicked.connect(self.button_point)
        self.ui.pushButton_16.clicked.connect(self.button_divide)
        self.ui.pushButton_17.clicked.connect(self.button_equal)

    def button_equal(self):
        equation = self.ui.label.text()
        self.i = 1
        ans = eval(equation)
        self.ui.label.setText(str(ans))

    def button0(self):
        if self.i == 1:
            self.ui.label.setText("")
        text = self.ui.label.text()
        if text != "0":
            self.ui.label.setText(text + "0")
            self.i = 0

    def button1(self):
        if self.i == 1:
            self.ui.label.setText("")
        text = self.ui.label.text()
        self.ui.label.setText(text + "1")
        self.i = 0

    def button2(self):
        if self.i == 1:
            self.ui.label.setText("")
        text = self.ui.label.text()
        self.ui.label.setText(text + "2")
        self.i = 0

    def button3(self):
        if self.i == 1:
            self.ui.label.setText("")
        text = self.ui.label.text()
        self.ui.label.setText(text + "3")
        self.i = 0

    def button4(self):
        if self.i == 1:
            self.ui.label.setText("")
        text = self.ui.label.text()
        self.ui.label.setText(text + "4")
        self.i = 0

    def button5(self):
        if self.i == 1:
            self.ui.label.setText("")
        text = self.ui.label.text()
        self.ui.label.setText(text + "5")
        self.i = 0

    def button6(self):
        if self.i == 1:
            self.ui.label.setText("")
        text = self.ui.label.text()
        self.ui.label.setText(text + "6")
        self.i = 0

    def button7(self):
        if self.i == 1:
            self.ui.label.setText("")
        text = self.ui.label.text()
        self.ui.label.setText(text + "7")
        self.i = 0

    def button8(self):
        if self.i == 1:
            self.ui.label.setText("")
        text = self.ui.label.text()
        self.ui.label.setText(text + "8")
        self.i = 0

    def button9(self):
        if self.i == 1:
            self.ui.label.setText("")
        text = self.ui.label.text()
        self.ui.label.setText(text + "9")
        self.i = 0

    def button_point(self):
        if self.i == 1:
            self.ui.label.setText("")
        if self.ui.label.text() != "":
            text = self.ui.label.text()
            self.ui.label.setText(text + ".")
        self.i = 0

    def button_add(self):
        if self.i == 1:
            self.ui.label.setText("")
        if self.ui.label.text() != "":
            text = self.ui.label.text()
            self.ui.label.setText(text + "+")
        self.i = 0

    def button_minus(self):
        if self.i == 1:
            self.ui.label.setText("")
        if self.ui.label.text() != "":
            text = self.ui.label.text()
            self.ui.label.setText(text + "-")
        self.i = 0

    def button_times(self):
        if self.i == 1:
            self.ui.label.setText("")
        if self.ui.label.text() != "":
            text = self.ui.label.text()
            self.ui.label.setText(text + "*")
        self.i = 0

    def button_divide(self):
        if self.i == 1:
            self.ui.label.setText("")
        if self.ui.label.text() != "":
            text = self.ui.label.text()
            self.ui.label.setText(text + "/")
        self.i = 0

    def button_Clear(self):
        self.ui.label.setText("")
        self.i = 0


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
