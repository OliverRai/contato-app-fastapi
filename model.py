from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

from sql_alchemy import Base


class Contato(Base):
    __table_name__ = "contatos"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    telephone = Column(Integer, nullable=False)


    address = relationship(
        "Address", back_populates="contato", cascade="all, delete-orphan"
    )


class Address(Base):
    __table_name__ = "contatos_address"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String)
    contato_id = Column(Integer, ForeignKey("contato.id"))  