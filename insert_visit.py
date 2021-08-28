import operator
from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore


class VisitModel:
    horse = ''
    employee = ''
    data = ''
    purpose = ''


class MyWindow(QtWidgets.QWidget):

    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self, *args)
        self.setGeometry(300, 200, 570, 450)
        layout = QtWidgets.QVBoxLayout(self)
        textH = QtWidgets.QLabel(text='Koń:')
        textE = QtWidgets.QLabel(text="Pracownik:")
        textD = QtWidgets.QLabel(text='Data:')
        textP = QtWidgets.QLabel(text='Cel wizyty:')

        self.inputH = QtWidgets.QLineEdit()
        self.inputE = QtWidgets.QLineEdit()
        self.inputD = QtWidgets.QLineEdit()
        self.inputP = QtWidgets.QLineEdit()

        layout.addWidget(textH)
        layout.addWidget(self.inputH)
        layout.addWidget(textE)
        layout.addWidget(self.inputE)
        layout.addWidget(textD)
        layout.addWidget(self.inputD)
        layout.addWidget(textP)
        layout.addWidget(self.inputP)


        self.buttonAdd = QtWidgets.QPushButton(text='Dodaj')
        self.buttonAdd.clicked.connect(self.AddToDB)

        layout.addWidget(self.buttonAdd)
        self.setLayout(layout)

    def AddToDB(self):
        visit = VisitModelModel()

        # pobieramy dane dla nowego obiektu z interfejsu:
        visit.horse = self.inputH.text()
        visit.employee = self.inputE.text()
        visit.date = self.inputD.text()
        visit.purpose = self.inputP.text()

        # zapis do bazy

app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec_()
