from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey, MetaData, DateTime
from sqlalchemy_utils import database_exists, create_database
import pymysql
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()
# połączenie się z bazą danych za pomocą create_engine
engine = create_engine("mysql+pymysql://root:@localhost/dbTEST")
metadata = MetaData(engine)
# opisywanie tabel z diagramu UML, opisywanie kolumn, ich pól i typów, tworzenie relacji między obiektami, kluczy głównych i obcych
Table('function', metadata,
      Column('id', Integer, primary_key=True, nullable=False),
      Column('name', String(50), nullable=False))

Table('user', metadata,
      Column('id', Integer, primary_key=True, nullable=False),
      Column('surname', String(50), nullable=True),
      Column('name', String(50), nullable=True),
      Column('address', String(50), nullable=True),
      Column('phone', String(50), nullable=True),
      Column('function_id', Integer, ForeignKey('function.id')))

Table('owner', metadata,
      Column('id', Integer, primary_key=True, nullable=False),
      Column('user_id', Integer, ForeignKey('user.id'), nullable=False))

Table('horse', metadata,
      Column('id', Integer, primary_key=True, nullable=False),
      Column('name', String(32), nullable=True),
      Column('mother', String(50), nullable=True),
      Column('father', String(50), nullable=True),
      Column('race', String(30), nullable=True),
      Column('birth', String(30), nullable=True),
      Column('sex', String(20), nullable=True),
      Column('owner_id', Integer, ForeignKey('owner.id'), nullable=True))

Table('stable', metadata,
      Column('id', Integer, primary_key=True, nullable=False),
      Column('name', String(100), nullable=True),
      Column('address', String(128), nullable=True))

Table('stable.horse', metadata,
      Column('id', Integer, primary_key=True, nullable=False),
      Column('stable_id', Integer, ForeignKey('stable.id'), nullable=True),
      Column('horse_id', Integer, ForeignKey('horse.id'), nullable=True),
      Column('date', DateTime))

Table('schedule', metadata,
      Column('id', Integer, primary_key=True, nullable=False),
      Column('date', DateTime),
      Column('fodder', String(128), nullable=True),
      Column('supplementation', String(128), nullable=True),
      Column('complementary_foods', String(128), nullable=True))

Table('feeding', metadata,
      Column('id', Integer, primary_key=True, nullable=False),
      Column('schedule_id', Integer, ForeignKey('schedule.id'), nullable=True),
      Column('user_id', Integer, ForeignKey('user.id'), nullable=True),
      Column('horse_id', Integer, ForeignKey('horse.id'), nullable=True),
      Column('date', DateTime, nullable=False, default=datetime))

Table('visit', metadata,
      Column('id', Integer, primary_key=True, nullable=False),
      Column('horse_id', Integer, ForeignKey('horse.id'), nullable=True),
      Column('user_id', Integer, ForeignKey('user.id'), nullable=True),
      Column('date', DateTime),
      Column('purpose', String(150), nullable=True))

metadata.create_all((engine))
print(database_exists(engine.url))


