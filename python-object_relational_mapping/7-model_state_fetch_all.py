#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    """create engine"""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)
    """ create session"""
    Base.metadata.create_all(engine)
    session = Session(engine)
    """quering data"""
    states = session.query(State).order_by(State.id).all()
    """ print instances"""
    for state in states:
        print("{}: {}".format(state.id, state.name))
