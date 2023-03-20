#!/usr/bin/python3
"""
a python file that contains the
class definition of a Model and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

Base = declarative_base()


class City(Base):
    """
    this defines a mysql table
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True,
                unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
