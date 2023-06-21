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
    prefix="/forensics",
    tags=['Forensics']
)

# CREATE A USER


@router.post("/", status_code=status.HTTP_201_CREATED,)
def create_new_forensic(input: dict, db: Session = Depends(get_db)):

    new_forensic = models.Forensic(**input)
    db.add(new_forensic)
    db.commit()
    db.refresh(new_forensic)

    return new_forensic.__dict__


# DELETE A USER


@router.delete("/{ID}", status_code=status.HTTP_204_NO_CONTENT,)
def delete_a_forensic(ID: int, db: Session = Depends(get_db)):

    forensic_query = db.query(models.Forensic).filter(
        models.Forensic.uid == ID)
    forensic = forensic_query.first()
    if forensic == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"forensic with id: {ID} does not exist")
    forensic_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# GET A USER


@ router.get("/{ID}",)
# , current_forensic: int = Depends(oauth2.get_current_forensic)):
def get_forensic(ID: int, db: Session = Depends(get_db)):

    forensic_query = db.query(models.Forensic).filter(
        models.Forensic.uid == ID)
    forensic = forensic_query.first()

    if forensic == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"forensic with id: {ID} does not exist")
    return forensic  # .__list__

# GET ALL FORENSICS


@ router.get("/")
def get_all_forensics(db: Session = Depends(get_db)):
    results = db.query(models.Forensic).all()

    return results


# UPDATE A USER
@ router.put("/{ID}")
def update_post(input: dict, ID: int, db: Session = Depends(get_db)):
    forensic_query = db.query(models.Forensic).filter(
        models.Forensic.uid == ID)
    forensic = forensic_query.first()

    if forensic == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"forensic with id: {ID} does not exist")

    forensic_query.update(input, synchronize_session=False)
    db.commit()
    return forensic_query.first()
