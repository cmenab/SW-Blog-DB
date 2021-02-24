import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table Users
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)
    email = Column(String(20), nullable=False)

class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table People
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    gender = Column(String(20), nullable=False)
    homeworld = Column(String(20), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    eye_color = Column(String(20), nullable=False)
    birth_year = Column(String(20), nullable=False)

class Favpeople(Base):
    __tablename__ = 'favpeople'
    # Here we define columns for the table Favpeople
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    people_id = Column(Integer, ForeignKey('people.id'))

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table Planets
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    climate = Column(String(20), nullable=False)
    terrain = Column(String(20), nullable=False)
    diameter = Column(Integer, nullable=False)
    surface_water = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)

class Favplanets(Base):
    __tablename__ = 'favplanets'
    # Here we define columns for the table Favplanets
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    planet_id = Column(Integer, ForeignKey('planets.id')) 

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')