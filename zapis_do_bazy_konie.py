from PySide2 import QtWidgets
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class HorseModel(Base):
    __tablename__ = 'horse'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    mother = Column(String(50))
    father = Column(String(50))
    race = Column(String(30))
    birth = Column(String(50))
    sex = Column(String(20))
    owner_id = Column(Integer, ForeignKey('owner.id'))

class OwnerModel(Base):
    __tablename__ = 'owner'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    horses = relationship("HorseModel")

class MyWindow(QtWidgets.QWidget):

    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self, *args)
        self.setGeometry(300, 200, 570, 450)
        layout = QtWidgets.QVBoxLayout(self)
        textN = QtWidgets.QLabel(text='Imie:')
        textM = QtWidgets.QLabel(text='Imię matki:')
        textF = QtWidgets.QLabel(text='Imię ojca:')
        textR = QtWidgets.QLabel(text='Rasa:')
        textB = QtWidgets.QLabel(text='Data urodzenia:')
        textS = QtWidgets.QLabel(text='Płeć:')
        textO = QtWidgets.QLabel(text='ID właściciela:')
        self.inputN = QtWidgets.QLineEdit()
        self.inputM = QtWidgets.QLineEdit()
        self.inputF = QtWidgets.QLineEdit()
        self.inputR = QtWidgets.QLineEdit()
        self.inputB = QtWidgets.QLineEdit()
        self.inputS = QtWidgets.QLineEdit()
        self.inputO = QtWidgets.QLineEdit()

        layout.addWidget(textN)
        layout.addWidget(self.inputN)
        layout.addWidget(textM)
        layout.addWidget(self.inputM)
        layout.addWidget(textF)
        layout.addWidget(self.inputF)
        layout.addWidget(textR)
        layout.addWidget(self.inputR)
        layout.addWidget(textB)
        layout.addWidget(self.inputB)
        layout.addWidget(textS)
        layout.addWidget(self.inputS)
        layout.addWidget(textO)
        layout.addWidget(self.inputO)

        self.buttonAdd = QtWidgets.QPushButton(text='Dodaj')
        self.buttonAdd.clicked.connect(self.AddToDB)

        layout.addWidget(self.buttonAdd)
        self.setLayout(layout)

    def AddToDB(self):
        horse = HorseModel()

        #pobieramy dane dla nowego obiektu z interfejsu:
        horse.name = self.inputN.text()
        horse.mother = self.inputM.text()
        horse.father = self.inputF.text()
        horse.race = self.inputR.text()
        horse.birth = self.inputB.text()
        horse.sex = self.inputS.text()
        horse.owner_id = self.inputO.text()

        #teraz zapisać do bazy
        sesja.add(horse)
        sesja.commit()
        sesja.close()


engine = create_engine("mysql+pymysql://root:@localhost/dbTEST")
BDSesja = sessionmaker(bind=engine)
sesja = BDSesja()
app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec_()
