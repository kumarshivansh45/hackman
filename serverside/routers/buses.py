from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
import models
import oauth2
import schemas
import utils
import json
from database import get_db

router = APIRouter(
    prefix="/buss",
    tags=['Buses']
)

# CREATE A USER


@router.post("/", status_code=status.HTTP_201_CREATED,)
def create_new_bus(input: dict, db: Session = Depends(get_db)):

    new_bus = models.Bus(**input)
    db.add(new_bus)
    db.commit()
    db.refresh(new_bus)

    return new_bus.__dict__


# DELETE A USER


@router.delete("/{ID}", status_code=status.HTTP_204_NO_CONTENT,)
def delete_a_bus(ID: int, db: Session = Depends(get_db)):

    bus_query = db.query(models.Bus).filter(
        models.Bus.uid == ID)
    bus = bus_query.first()
    if bus == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"bus with id: {ID} does not exist")
    bus_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# GET A USER


@ router.get("/{ID}",)
# , current_bus: int = Depends(oauth2.get_current_bus)):
def get_bus(ID: int, db: Session = Depends(get_db)):

    bus_query = db.query(models.Bus).filter(
        models.Bus.uid == ID)
    bus = bus_query.first()

    if bus == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"bus with id: {ID} does not exist")
    return bus  # .__list__

# GET ALL BUSS


@ router.get("/")
def get_all_buss(db: Session = Depends(get_db)):
    results = db.query(models.Bus).all()

    return results


# UPDATE A USER
@ router.put("/{ID}")
def update_post(input: dict, ID: int, db: Session = Depends(get_db)):
    bus_query = db.query(models.Bus).filter(
        models.Bus.uid == ID)
    bus = bus_query.first()

    if bus == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"bus with id: {ID} does not exist")

    bus_query.update(input, synchronize_session=False)
    db.commit()
    return bus_query.first()
