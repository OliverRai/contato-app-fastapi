from sqlalchemy import Column, String, Integer

from settings_bd import Base

class Person(Base):
    __tablename__ = 'person'
    
    id: int = Column(Integer, primary_key=True ,autoincrement=True)
    name: str = Column(String(40), nullable=False)
    cellphone: str = Column(String(15), nullable=False)
    email: str = Column(String(50))