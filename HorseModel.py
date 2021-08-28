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