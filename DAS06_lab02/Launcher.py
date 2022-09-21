import sys

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('prog.ui', self)

        self.setWindowTitle('Дроздов А. С. ВТиП-302 Lab2')

        self.pushButton_solver.clicked.connect(self.solve)
        self.pushButton_cleaner.clicked.connect(self.clean)
        self.pushButton_exiter.clicked.connect(self.close)


    def solve(self):
        try:
            a = float(self.lineEdit_a.text())
            b = float(self.lineEdit_b.text())
            x = float(self.lineEdit_x.text())

            if x < 4:
                answer = (x * x * x) - (a * b)
            else:
                answer = (x + 4 * a)/(a * a * b * b)
            self.label_answer.setText(' Ответ: ' + str(format(answer, '.2f')))
            self.label_answer.setStyleSheet('background: rgb(0, 255, 0, 0.5); color: rgb(255, 255, 255, 1);')
        except:
            self.label_answer.setText(' Ошибка!')
            self.label_answer.setStyleSheet('background: rgb(255, 0, 0, 0.5); color: rgb(255, 255, 255, 1);')

    def clean(self):
        self.lineEdit_a.setText('')
        self.lineEdit_b.setText('')
        self.lineEdit_x.setText('')
        self.label_answer.setText('Ответ: ')
        self.label_answer.setStyleSheet('')


app = QApplication(sys.argv)
window = Main()
window.show()
sys.exit(app.exec_())


