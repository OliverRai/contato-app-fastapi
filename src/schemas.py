from pydantic import BaseModel

class PersonBase(BaseModel):
    name: str
    cellphone: str
    email: str

class AddressBase(BaseModel):
    city: str
    distric: str
    number: str

class PersonRequest(PersonBase):
    ...

class PersonResponse(PersonBase):
    id: int

    class Config:
        orm_mode = True