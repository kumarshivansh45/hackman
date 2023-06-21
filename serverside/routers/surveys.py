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
    prefix="/surveys",
    tags=['Surveys']
)

# CREATE A USER


@router.post("/", status_code=status.HTTP_201_CREATED,)
def create_new_survey(input: dict, db: Session = Depends(get_db)):

    new_survey = models.Survey(**input)
    db.add(new_survey)
    db.commit()
    db.refresh(new_survey)

    return new_survey.__dict__


# DELETE A USER


@router.delete("/{ID}", status_code=status.HTTP_204_NO_CONTENT,)
def delete_a_survey(ID: int, db: Session = Depends(get_db)):

    survey_query = db.query(models.Survey).filter(
        models.Survey.uid == ID)
    survey = survey_query.first()
    if survey == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"survey with id: {ID} does not exist")
    survey_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# GET A USER


@ router.get("/{ID}",)
# , current_survey: int = Depends(oauth2.get_current_survey)):
def get_survey(ID: int, db: Session = Depends(get_db)):

    survey_query = db.query(models.Survey).filter(
        models.Survey.uid == ID)
    survey = survey_query.first()

    if survey == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"survey with id: {ID} does not exist")
    return survey  # .__list__

# GET ALL SURVEYS


@ router.get("/")
def get_all_surveys(db: Session = Depends(get_db)):
    results = db.query(models.Survey).all()

    return results


# UPDATE A USER
@ router.put("/{ID}")
def update_post(input: dict, ID: int, db: Session = Depends(get_db)):
    survey_query = db.query(models.Survey).filter(
        models.Survey.uid == ID)
    survey = survey_query.first()

    if survey == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"survey with id: {ID} does not exist")

    survey_query.update(input, synchronize_session=False)
    db.commit()
    return survey_query.first()
