from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from models.model import Person
from settings_bd import engine, Base, get_db
from person_repository import PersonRepository
from schemas import PersonRequest, PersonResponse


Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.post("/api/v1/contact", response_model=PersonResponse, status_code=status.HTTP_201_CREATED)
def create(request: PersonRequest, db: Session = Depends(get_db)):
    person = PersonRepository.save(db, Person(**request.dict()))
    return PersonResponse.from_orm(person)


@app.get("/api/v1/contact", response_model=list[PersonResponse])
def find_all(db: Session = Depends(get_db)):
    contacts = PersonRepository.find_all(db)
    return [PersonResponse.from_orm(person) for person in contacts]


@app.get("/api/v1/contact/{id}", response_model = PersonResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    contact = PersonRepository.find_by_id(db, id)
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Not Found"
        )
    return contact