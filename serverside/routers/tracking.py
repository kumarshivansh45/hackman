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
    prefix="/trackings",
    tags=['Trackings']
)

# CREATE A USER


@router.post("/", status_code=status.HTTP_201_CREATED,)
def create_new_tracking(input: dict, db: Session = Depends(get_db)):

    new_tracking = models.Tracking(**input)
    db.add(new_tracking)
    db.commit()
    db.refresh(new_tracking)

    return new_tracking.__dict__


# DELETE A USER


@router.delete("/{ID}", status_code=status.HTTP_204_NO_CONTENT,)
def delete_a_tracking(ID: int, db: Session = Depends(get_db)):

    tracking_query = db.query(models.Tracking).filter(
        models.Tracking.uid == ID)
    tracking = tracking_query.first()
    if tracking == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"tracking with id: {ID} does not exist")
    tracking_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# GET A USER


@ router.get("/{ID}",)
# , current_tracking: int = Depends(oauth2.get_current_tracking)):
def get_tracking(ID: int, db: Session = Depends(get_db)):

    tracking_query = db.query(models.Tracking).filter(
        models.Tracking.uid == ID)
    tracking = tracking_query.first()

    if tracking == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"tracking with id: {ID} does not exist")
    return tracking  # .__list__

# GET ALL TRACKINGS


@ router.get("/")
def get_all_trackings(db: Session = Depends(get_db)):
    results = db.query(models.Tracking).all()

    return results


# UPDATE A USER
@ router.put("/{ID}")
def update_post(input: dict, ID: int, db: Session = Depends(get_db)):
    tracking_query = db.query(models.Tracking).filter(
        models.Tracking.uid == ID)
    tracking = tracking_query.first()

    if tracking == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"tracking with id: {ID} does not exist")

    tracking_query.update(input, synchronize_session=False)
    db.commit()
    return tracking_query.first()
