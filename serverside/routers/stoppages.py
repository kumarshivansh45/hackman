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
    prefix="/stoppages",
    tags=['Stoppages']
)

# CREATE A USER


@router.post("/", status_code=status.HTTP_201_CREATED,)
def create_new_stoppage(input: dict, db: Session = Depends(get_db)):

    new_stoppage = models.Stoppage(**input)
    db.add(new_stoppage)
    db.commit()
    db.refresh(new_stoppage)

    return new_stoppage.__dict__


# DELETE A USER


@router.delete("/{ID}", status_code=status.HTTP_204_NO_CONTENT,)
def delete_a_stoppage(ID: int, db: Session = Depends(get_db)):

    stoppage_query = db.query(models.Stoppage).filter(
        models.Stoppage.uid == ID)
    stoppage = stoppage_query.first()
    if stoppage == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"stoppage with id: {ID} does not exist")
    stoppage_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# GET A USER


@ router.get("/{ID}",)
# , current_stoppage: int = Depends(oauth2.get_current_stoppage)):
def get_stoppage(ID: int, db: Session = Depends(get_db)):

    stoppage_query = db.query(models.Stoppage).filter(
        models.Stoppage.uid == ID)
    stoppage = stoppage_query.first()

    if stoppage == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"stoppage with id: {ID} does not exist")
    return stoppage  # .__list__

# GET ALL STOPPAGES


@ router.get("/")
def get_all_stoppages(db: Session = Depends(get_db)):
    results = db.query(models.Stoppage).all()

    return results


# UPDATE A USER
@ router.put("/{ID}")
def update_post(input: dict, ID: int, db: Session = Depends(get_db)):
    stoppage_query = db.query(models.Stoppage).filter(
        models.Stoppage.uid == ID)
    stoppage = stoppage_query.first()

    if stoppage == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"stoppage with id: {ID} does not exist")

    stoppage_query.update(input, synchronize_session=False)
    db.commit()
    return stoppage_query.first()
