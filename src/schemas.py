from pydantic import BaseModel

class PersonBase(BaseModel):
    name: str
    cellphone: str
    email: str

class PersonRequest(PersonBase):
    ...

class PersonResponse(PersonBase):
    id: int

    class Config:
        orm_mode = True