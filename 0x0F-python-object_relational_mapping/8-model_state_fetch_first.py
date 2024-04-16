#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:]

    # Connect to MySQL server
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                          .format(username, password, database),
                          pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get the first state ordered by ID
    state = session.query(State).order_by(State.id).first()

    # Print the state information
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))  # Corrected formatting

    # Close the session
    session.close()

