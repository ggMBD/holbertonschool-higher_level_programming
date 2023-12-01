#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    """create engine"""
    path = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1],
            argv[2],
            argv[3])
    engine = create_engine(path)
    """ create session"""
    Base.metadata.create_all(engine)
    session = Session(engine)
    """quering data"""
    states = session.query(State).order_by(State.id).all()
    """ print instances"""
    for state in states:
        print("{}: {}".format(state.id, state.name))
