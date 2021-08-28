import operator
from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore

class Stable_horseModel:
    date = ''


class MyWindow(QtWidgets.QWidget):

    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self, *args)
        self.setGeometry(300, 200, 570, 150)
        layout = QtWidgets.QVBoxLayout(self)
        textD = QtWidgets.QLabel(text='Data:')

        self.inputD = QtWidgets.QLineEdit()

        layout.addWidget(textD)
        layout.addWidget(self.inputD)

        self.buttonAdd = QtWidgets.QPushButton(text='Dodaj')
        self.buttonAdd.clicked.connect(self.AddToDB)

        layout.addWidget(self.buttonAdd)
        self.setLayout(layout)

    def AddToDB(self):
        stable_horse = Stable_horseModel()

        # pobieramy dane dla nowego obiektu z interfejsu:
        stable_horse.name = self.inputD.text()

        # zapis do bazy


app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec_()
