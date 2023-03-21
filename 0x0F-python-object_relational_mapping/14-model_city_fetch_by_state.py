#!/usr/bin/python3
"""a script that lists all State objects that contain the letter a
"""
from sys import argv
from model_state import Base, State
from model_city import Base, City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engineCon = 'mysql+mysqldb://{}:{}@localhost/{}'.\
            format(argv[1], argv[2], argv[3])
    engine = create_engine(engineCon, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(City.id, City.name, State.name)\
            .join(State, City.state_id == State.id)\
            .order_by(City.id.asc())
    result = query.all()
    for row in result:
        print(f"{row[2]}: ({row[0]}) {row[1]}")
