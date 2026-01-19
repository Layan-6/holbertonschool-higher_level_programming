#!/usr/bin/python3
"""
Contains the class definition of a State
and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create a declarative base instance
Base = declarative_base()


class State(Base):
    """
    State class that links to the MySQL table 'states'
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    # This allows the script to create the table when run directly
    import sys
    
    if len(sys.argv) != 4:
        print("Usage: ./model_state.py <mysql username> <mysql password> <database name>")
        sys.exit(1)
        
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    # Create engine and connect to database
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
        pool_pre_ping=True
    )
    
    # Create all tables defined by classes that inherit from Base
    Base.metadata.create_all(engine)
    print(f"Table 'states' created successfully in database '{database}'")
