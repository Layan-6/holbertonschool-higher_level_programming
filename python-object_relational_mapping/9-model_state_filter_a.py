#!/usr/bin/python3
"""
Case-insensitive search for 'a' or 'A'
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./9-model_state_filter_a.py <username> "
              "<password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@'
        f'localhost:3306/{database}',
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Case-insensitive search (finds both 'a' and 'A')
    states = session.query(State).filter(
        func.lower(State.name).like('%a%')
    ).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
