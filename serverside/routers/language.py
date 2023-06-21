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
    prefix="/languages",
    tags=['Languages']
)

# CREATE A USER


@router.post("/", status_code=status.HTTP_201_CREATED,)
def create_new_language(input: dict, db: Session = Depends(get_db)):

    new_language = models.Language(**input)
    db.add(new_language)
    db.commit()
    db.refresh(new_language)

    return new_language.__dict__


# DELETE A USER


@router.delete("/{ID}", status_code=status.HTTP_204_NO_CONTENT,)
def delete_a_language(ID: int, db: Session = Depends(get_db)):

    language_query = db.query(models.Language).filter(
        models.Language.uid == ID)
    language = language_query.first()
    if language == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"language with id: {ID} does not exist")
    language_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# GET A USER


@ router.get("/{ID}",)
# , current_language: int = Depends(oauth2.get_current_language)):
def get_language(ID: int, db: Session = Depends(get_db)):

    language_query = db.query(models.Language).filter(
        models.Language.uid == ID)
    language = language_query.first()

    if language == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"language with id: {ID} does not exist")
    return language  # .__list__

# GET ALL LANGUAGES


@ router.get("/")
def get_all_languages(db: Session = Depends(get_db)):
    results = db.query(models.Language).all()

    return results


# UPDATE A USER
@ router.put("/{ID}")
def update_post(input: dict, ID: int, db: Session = Depends(get_db)):
    language_query = db.query(models.Language).filter(
        models.Language.uid == ID)
    language = language_query.first()

    if language == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"language with id: {ID} does not exist")

    language_query.update(input, synchronize_session=False)
    db.commit()
    return language_query.first()
