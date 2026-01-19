#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get command line arguments
    if len(sys.argv) != 4:
        print("Usage: ./7-model_state_fetch_all.py <username> "
              "<password> <database>")
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    # Create engine and connect to database
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@'
        f'localhost:3306/{database}',
        pool_pre_ping=True
    )
    
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    
    # Create a Session instance
    session = Session()
    
    # Query all State objects, ordered by id
    states = session.query(State).order_by(State.id).all()
    
    # Display results
    for state in states:
        print(f"{state.id}: {state.name}")
    
    # Close the session
    session.close()
