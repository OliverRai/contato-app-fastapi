from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from settings_bd import Base

class Person(Base):
    __tablename__ = 'person_table'
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(40), nullable=False)
    cellphone: str = Column(String(15), nullable=False)
    email: str = Column(String(50))

    address = relationship('Address', back_populates='person')


class Address(Base):
    __tablename__ = 'address_table'
    
    id: int = Column(Integer, autoincrement=True, primary_key=True)
    city: str = Column(String)
    district: str = Column(String)
    number: int = Column(Integer)

    person_id: str = Column(Integer, ForeignKey('person_table.id'))
    person = relationship('Person', back_populates='address')
