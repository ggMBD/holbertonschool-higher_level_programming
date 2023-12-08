#!/usr/bin/python3
"""python file that contains the class definition of a State
and an instance Base = declarative_base()"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """State class that links to the states table in the MySQL database"""

    __tablename__ = 'states'

    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement=True
                )
    name = Column(String(128), nullable=False)
