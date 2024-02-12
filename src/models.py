import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    mail = Column(String(100), unique=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    contraseña = Column(String(100), nullable=False)

class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    color = Column(Enum)
    tamaño = Column(Integer, nullable=False)

    def to_dict(self):
        return {}

class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    color = Column(String(100), nullable=False)    
    
    def to_dict(self):
        return {}
    
class Favoritos(Base):
    __tablename__ = 'favoritos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    usuarioId = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    planetasId = Column(String(50), ForeignKey('planetas.id'), nullable=True)
    personajesId = Column(String(50), ForeignKey('personajes.id'), nullable=True)
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
