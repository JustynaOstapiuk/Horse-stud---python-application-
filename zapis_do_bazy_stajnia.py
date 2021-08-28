from PySide2 import QtWidgets
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StableModel(Base):
    __tablename__ = 'stable'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    address = Column(String(150))

class MyWindow(QtWidgets.QWidget):

    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self, *args)
        self.setGeometry(300, 200, 570, 150)
        layout = QtWidgets.QVBoxLayout(self)
        textN = QtWidgets.QLabel(text='Nazwa:')
        textA = QtWidgets.QLabel(text='Adres:')

        self.inputN = QtWidgets.QLineEdit()
        self.inputA = QtWidgets.QLineEdit()

        layout.addWidget(textN)
        layout.addWidget(self.inputN)
        layout.addWidget(textA)
        layout.addWidget(self.inputA)

        self.buttonAdd = QtWidgets.QPushButton(text='Dodaj')
        self.buttonAdd.clicked.connect(self.AddToDB)

        layout.addWidget(self.buttonAdd)
        self.setLayout(layout)

    def AddToDB(self):
        stable = StableModel()

        # pobieramy dane dla nowego obiektu z interfejsu:
        stable.name = self.inputN.text()
        stable.address = self.inputA.text()

        # teraz zapisać do bazy
        sesja.add(stable)
        sesja.commit()
        sesja.close()


engine = create_engine("mysql+pymysql://root:@localhost/dbTEST")
BDSesja = sessionmaker(bind=engine)
sesja = BDSesja()
app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec_()
