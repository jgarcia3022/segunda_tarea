from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import delete
from sqlalchemy import update

engine = create_engine('sqlite:///NuevaBd.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
