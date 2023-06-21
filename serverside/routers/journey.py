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
    prefix="/journeys",
    tags=['Journeys']
)

# CREATE A USER


@router.post("/", status_code=status.HTTP_201_CREATED,)
def create_new_journey(input: dict, db: Session = Depends(get_db)):

    new_journey = models.Journey(**input)
    db.add(new_journey)
    db.commit()
    db.refresh(new_journey)

    return new_journey.__dict__


# DELETE A USER


@router.delete("/{ID}", status_code=status.HTTP_204_NO_CONTENT,)
def delete_a_journey(ID: int, db: Session = Depends(get_db)):

    journey_query = db.query(models.Journey).filter(
        models.Journey.uid == ID)
    journey = journey_query.first()
    if journey == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"journey with id: {ID} does not exist")
    journey_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# GET A USER


@ router.get("/{ID}",)
# , current_journey: int = Depends(oauth2.get_current_journey)):
def get_journey(ID: int, db: Session = Depends(get_db)):

    journey_query = db.query(models.Journey).filter(
        models.Journey.uid == ID)
    journey = journey_query.first()

    if journey == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"journey with id: {ID} does not exist")
    return journey  # .__list__

# GET ALL JOURNEYS


@ router.get("/")
def get_all_journeys(db: Session = Depends(get_db)):
    results = db.query(models.Journey).all()

    return results


# UPDATE A USER
@ router.put("/{ID}")
def update_post(input: dict, ID: int, db: Session = Depends(get_db)):
    journey_query = db.query(models.Journey).filter(
        models.Journey.uid == ID)
    journey = journey_query.first()

    if journey == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"journey with id: {ID} does not exist")

    journey_query.update(input, synchronize_session=False)
    db.commit()
    return journey_query.first()
