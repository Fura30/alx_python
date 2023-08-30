#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))

    # Create session factory
    Session = sessionmaker(bind=engine)

    # Create session
    session = Session()

    # Query the first State object
    state = session.query(State).order_by(State.id).first()

    # Check if state is None (table is empty)
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
