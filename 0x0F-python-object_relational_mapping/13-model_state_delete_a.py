#!/usr/bin/python3
"""a script that lists all State objects that contain the letter a
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engineCon = 'mysql+mysqldb://{}:{}@localhost/{}'.\
            format(argv[1], argv[2], argv[3])
    engine = create_engine(engineCon, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(State).filter(State.name.like('%a%')).delete()
    session.commit()
