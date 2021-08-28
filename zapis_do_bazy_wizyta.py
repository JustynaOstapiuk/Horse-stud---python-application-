from PySide2 import QtWidgets
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Integer, ForeignKey, String, Column, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    visits = relationship("VisitModel")

class HorseModel(Base):
    __tablename__ = 'horse'
    id = Column(Integer, primary_key=True, autoincrement=True)
    visits = relationship("VisitModel")

class VisitModel(Base):
    __tablename__ = 'visit'
    id = Column(Integer, primary_key=True, autoincrement=True)
    horse_id = Column(Integer, ForeignKey('horse.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    date = Column(datetime.datetime.today())
    purpose = Column(String(150))

class MyWindow(QtWidgets.QWidget):

    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self, *args)
        self.setGeometry(300, 200, 570, 450)
        layout = QtWidgets.QVBoxLayout(self)
        textH = QtWidgets.QLabel(text='ID konia:')
        textU = QtWidgets.QLabel(text='ID użytkownika:')
        textD = QtWidgets.QLabel(text='Data:')
        textP = QtWidgets.QLabel(text='Cel wizyty:')

        self.inputH = QtWidgets.QLineEdit()
        self.inputU = QtWidgets.QLineEdit()
        self.inputD = QtWidgets.QLineEdit()
        self.inputP = QtWidgets.QLineEdit()

        layout.addWidget(textH)
        layout.addWidget(self.inputH)
        layout.addWidget(textU)
        layout.addWidget(self.inputU)
        layout.addWidget(textD)
        layout.addWidget(self.inputD)
        layout.addWidget(textP)
        layout.addWidget(self.inputP)

        self.buttonAdd = QtWidgets.QPushButton(text='Dodaj')
        self.buttonAdd.clicked.connect(self.AddToDB)

        layout.addWidget(self.buttonAdd)
        self.setLayout(layout)

    def AddToDB(self):
        visit = VisitModel()

        # pobieramy dane dla nowego obiektu z interfejsu:
        visit.horse_id = self.inputH.text()
        visit.user_id = self.inputU.text()
        visit.date = self.inputD.text()
        visit.purpose = self.inputP.text()

        # teraz zapisać do bazy
        sesja.add(visit)
        sesja.commit()
        sesja.close()


engine = create_engine("mysql+pymysql://root:@localhost/dbTEST")
BDSesja = sessionmaker(bind=engine)
sesja = BDSesja()
app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec_()
