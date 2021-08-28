import operator
from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class StableModel:
    address = ''

class MyWindow(QtWidgets.QWidget):

    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self, *args)
        self.setGeometry(300, 200, 570, 150)
        layout = QtWidgets.QVBoxLayout(self)
        textA = QtWidgets.QLabel(text='Adres:')

        self.inputA = QtWidgets.QLineEdit()

        layout.addWidget(textA)
        layout.addWidget(self.inputA)

        self.buttonAdd = QtWidgets.QPushButton(text='Dodaj')
        self.buttonAdd.clicked.connect(self.AddToDB)

        layout.addWidget(self.buttonAdd)
        self.setLayout(layout)

    def AddToDB(self):
        stable = StableModel()

        # pobieramy dane dla nowego obiektu z interfejsu:
        stable.address = self.inputA.text()

        # zapis do bazy
        sesja.add(stable)
        sesja.commit()
        sesja.close()

engine = create_engine("mysql+pymysql://root:@localhost/newdb2")
BDSesja = sessionmaker(bind=engine)
sesja = BDSesja()
app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec_()
