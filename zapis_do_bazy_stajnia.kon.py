from PySide2 import QtWidgets
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class StableModel(Base):
    __tablename__ = 'stable'
    id = Column(Integer, primary_key=True, autoincrement=True)
    stables_horse = relationship("Stable_horseModel")

class Stable_horseModel(Base):
    __tablename__ = 'stable.horse'
    id = Column(Integer, primary_key=True, autoincrement=True)
    stable_id = Column(Integer, ForeignKey('stable.id'))
    horse_id = Column(Integer, ForeignKey('horse.id'))
    date = Column(DateTime)

class HorseModel(Base):
    __tablename__ = 'horse'
    id = Column(Integer, primary_key=True, autoincrement=True)
    stables_horse = relationship("Stable_horseModel")

class MyWindow(QtWidgets.QWidget):

    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self, *args)
        self.setGeometry(300, 200, 570, 150)
        layout = QtWidgets.QVBoxLayout(self)
        textS = QtWidgets.QLabel(text='ID stajni:')
        textH = QtWidgets.QLabel(text='ID konia:')
        textD = QtWidgets.QLabel(text='Data:')

        self.inputS = QtWidgets.QLineEdit()
        self.inputH = QtWidgets.QLineEdit()
        self.inputD = QtWidgets.QLineEdit()

        layout.addWidget(textS)
        layout.addWidget(self.inputS)
        layout.addWidget(textH)
        layout.addWidget(self.inputH)
        layout.addWidget(textD)
        layout.addWidget(self.inputD)

        self.buttonAdd = QtWidgets.QPushButton(text='Dodaj')
        self.buttonAdd.clicked.connect(self.AddToDB)

        layout.addWidget(self.buttonAdd)
        self.setLayout(layout)

    def AddToDB(self):
        stable_horse = Stable_horseModel()

        # pobieramy dane dla nowego obiektu z interfejsu:
        stable_horse.stable_id = self.inputS.text()
        stable_horse.horse_id = self.inputH.text()
        stable_horse.date = self.inputD.text()

        # teraz zapisać do bazy
        sesja.add(stable_horse)
        sesja.commit()
        sesja.close()


engine = create_engine("mysql+pymysql://root:@localhost/dbTEST")
BDSesja = sessionmaker(bind=engine)
sesja = BDSesja()
app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec_()
