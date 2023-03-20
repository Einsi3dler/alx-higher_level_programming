#!/usr/bin/python3
"""a script that lists the first State objects
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).order_by(State.id).first()
    if instance is None:
        print("Nothing")
    else:
        print(f"{instance.id}: {instance.name}")
