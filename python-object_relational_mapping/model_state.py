#!/usr/bin/python3
"""
Start link class to table in database
"""

import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class State(Base):
    """ State class """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    
    # Create all defined tables in the database
    Base.metadata.create_all(engine)
 

#Here's how the code works:

#1. It imports the necessary modules:  sys  for command-line arguments,  Column ,  Integer , and  String  for defining the table columns, and  create_engine  for connecting to the database.
#2. The  declarative_base()  function is used to create a base class that our  State  class will inherit from.
#3. The  State  class is defined with the required attributes and mapping to the  states  table.
#4. Inside the  if __name__ == "__main__":  block, an SQLAlchemy engine is created with the provided MySQL connection string.
#5.  Base.metadata.create_all(engine)  is called to create the tables in the database based on the defined classes.

#Remember to replace  'root' ,  'root' , and  'hbtn_0e_6_usa'  with your actual MySQL username, password, and database name.

#Make sure you have the necessary dependencies installed. You can install them using the following command:

# bash
#pip install sqlalchemy
# 

#After running the script, the  states  table should be created in your MySQL database with the specified columns.