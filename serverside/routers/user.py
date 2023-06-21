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
    prefix="/users",
    tags=['Users']
)

# CREATE A USER


@router.post("/", status_code=status.HTTP_201_CREATED,)
def create_new_user(input: dict, db: Session = Depends(get_db)):

    if input["password"] == input["conf_password"]:

        values = input.pop("conf_password")
        new_user = models.User(**input)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user.__dict__
    else:
        return {"message": "passwd & conf_passwd dont match"}

# DELETE A USER


@router.delete("/{ID}", status_code=status.HTTP_204_NO_CONTENT,)
def delete_a_user(ID: int, db: Session = Depends(get_db)):

    user_query = db.query(models.User).filter(models.User.uid == ID)
    user = user_query.first()
    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id: {ID} does not exist")
    user_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# GET A USER


@ router.get("/{ID}",)
# , current_user: int = Depends(oauth2.get_current_user)):
def get_user(ID: int, db: Session = Depends(get_db)):

    user_query = db.query(models.User).filter(
        models.User.uid == ID)
    user = user_query.first()

    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id: {ID} does not exist")
    return user  # .__list__

# GET ALL USERS


@ router.get("/")
def get_all_users(db: Session = Depends(get_db)):
    results = db.query(models.User).all()

    return results


# UPDATE A USER
@ router.put("/{ID}")
def update_post(input: dict, ID: int, db: Session = Depends(get_db)):
    user_query = db.query(models.User).filter(
        models.User.uid == ID)
    user = user_query.first()

    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id: {ID} does not exist")
    if (input["conf_password"] == input["password"]):
        value = input.pop("conf_password")

        user_query.update(input, synchronize_session=False)
        db.commit()
        return user_query.first()

    else:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED,
                            detail=f"passwd & conf_passwd dont match")
