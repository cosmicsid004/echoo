#this files creates the stucture of the tables in database

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from database import Base
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    disables = Column(Boolean, default=False)

    eechos = relationship('Eecho', back_populates="creator")

    
class Eecho(Base):
    __tablename__ = 'eechos'

    id = Column(Integer, primary_key=True, index=True)
    body = Column(String)
    user_id = Column(Integer, ForeignKey ('users.id'))
    timeStamp = Column(DateTime, default=datetime.utcnow)

    creator = relationship("User", back_populates="eechos")
