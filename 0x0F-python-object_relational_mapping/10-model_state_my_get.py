#!/usr/bin/python3
"""a script that prints the State object with the name passed as argument
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
    instance = session.query(State).order_by(State.id).\
        filter(State.name == argv[4]).first()
    if instance is None:
        print("Not found")
    else:
        print(instance.id)
