from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from sql_alchemy import Base


class Contato(Base):
    __table_name__ = "contatos"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    telephone = Column(Integer, nullable=False)


    address = relationship("Address", back_populates="contato", cascade="all, delete-orphan")

    def __repr__(self):
        return f'Contato (id={self.id}, name={self.name}, telephone={self.telephone})'
    

class Address(Base):
    __table_name__ = "address"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String)
    contato_id = Column(Integer, ForeignKey("contato.id"))  

    user = relationship("Contato", back_populates="address")

    def __repr__(self):
        return f'Address (id={self.id}, email={self.email})'