import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)


class character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    birth_year = Column(String(250))
    eye_color = Column(String(250))
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    gender = Column(String(250))
    height = Column(String(250))
    mass = Column(String(250))
    homeworld = Column(String(250))
    films = Column(String(250))
    species = Column(String(250))
    starships = Column(String(250))
    vehicles = Column(String(250))

class planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    climate = Column(String(250))
    diameter = Column(String(250))
    gravity = Column(String(250))
    orbital_period = Column(String(250))
    population = Column(String(250))
    rotation_period = Column(String(250))
    surface_water = Column(String(250))
    terrain = Column(String(250))

class starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    MGLT = Column(String(250))
    cargo_capacity = Column(String(250))
    consumable = Column(String(250))
    cost_in_credits = Column(String(250))
    crew = Column(String(250))
    hyperdrive_rating = Column(String(250))
    length = Column(String(250))
    manufacturer = Column(String(250))
    max_atmospherix_speed = Column(String(250))

class favorite_character(Base):
    __tablename__ = 'favorite_character'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))

class favorite_planet(Base):
    __tablename__ = 'favorite_planet'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))

class favorite_starship(Base):
    __tablename__ = 'favorite_starship'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    starship_id = Column(Integer, ForeignKey('starship.id'))


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
