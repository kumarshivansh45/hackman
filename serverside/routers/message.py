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
    prefix="/messages",
    tags=['Messages']
)

# CREATE A USER


@router.post("/", status_code=status.HTTP_201_CREATED,)
def create_new_message(input: dict, db: Session = Depends(get_db)):

    new_message = models.Message(**input)
    db.add(new_message)
    db.commit()
    db.refresh(new_message)

    return new_message.__dict__


# DELETE A USER


@router.delete("/{ID}", status_code=status.HTTP_204_NO_CONTENT,)
def delete_a_message(ID: int, db: Session = Depends(get_db)):

    message_query = db.query(models.Message).filter(
        models.Message.uid == ID)
    message = message_query.first()
    if message == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"message with id: {ID} does not exist")
    message_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# GET A USER


@ router.get("/{ID}",)
# , current_message: int = Depends(oauth2.get_current_message)):
def get_message(ID: int, db: Session = Depends(get_db)):

    message_query = db.query(models.Message).filter(
        models.Message.uid == ID)
    message = message_query.first()

    if message == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"message with id: {ID} does not exist")
    return message  # .__list__

# GET ALL MESSAGES


@ router.get("/")
def get_all_messages(db: Session = Depends(get_db)):
    results = db.query(models.Message).all()

    return results


# UPDATE A USER
@ router.put("/{ID}")
def update_post(input: dict, ID: int, db: Session = Depends(get_db)):
    message_query = db.query(models.Message).filter(
        models.Message.uid == ID)
    message = message_query.first()

    if message == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"message with id: {ID} does not exist")

    message_query.update(input, synchronize_session=False)
    db.commit()
    return message_query.first()
