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
    prefix="/data_confs",
    tags=['Data_confs']
)

# CREATE A USER


@router.post("/", status_code=status.HTTP_201_CREATED,)
def create_new_data_conf(input: dict, db: Session = Depends(get_db)):

    new_data_conf = models.Data_conf(**input)
    db.add(new_data_conf)
    db.commit()
    db.refresh(new_data_conf)

    return new_data_conf.__dict__


# DELETE A USER


@router.delete("/{ID}", status_code=status.HTTP_204_NO_CONTENT,)
def delete_a_data_conf(ID: int, db: Session = Depends(get_db)):

    data_conf_query = db.query(models.Data_conf).filter(
        models.Data_conf.uid == ID)
    data_conf = data_conf_query.first()
    if data_conf == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"data_conf with id: {ID} does not exist")
    data_conf_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# GET A USER


@ router.get("/{ID}",)
# , current_data_conf: int = Depends(oauth2.get_current_data_conf)):
def get_data_conf(ID: int, db: Session = Depends(get_db)):

    data_conf_query = db.query(models.Data_conf).filter(
        models.Data_conf.uid == ID)
    data_conf = data_conf_query.first()

    if data_conf == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"data_conf with id: {ID} does not exist")
    return data_conf  # .__list__

# GET ALL DATA_CONFS


@ router.get("/")
def get_all_data_confs(db: Session = Depends(get_db)):
    results = db.query(models.Data_conf).all()

    return results


# UPDATE A USER
@ router.put("/{ID}")
def update_post(input: dict, ID: int, db: Session = Depends(get_db)):
    data_conf_query = db.query(models.Data_conf).filter(
        models.Data_conf.uid == ID)
    data_conf = data_conf_query.first()

    if data_conf == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"data_conf with id: {ID} does not exist")

    data_conf_query.update(input, synchronize_session=False)
    db.commit()
    return data_conf_query.first()
