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
    prefix="/system_confs",
    tags=['System_confs']
)

# CREATE A USER


@router.post("/", status_code=status.HTTP_201_CREATED,)
def create_new_system_conf(input: dict, db: Session = Depends(get_db)):

    new_system_conf = models.System_conf(**input)
    db.add(new_system_conf)
    db.commit()
    db.refresh(new_system_conf)

    return new_system_conf.__dict__


# DELETE A USER


@router.delete("/{ID}", status_code=status.HTTP_204_NO_CONTENT,)
def delete_a_system_conf(ID: int, db: Session = Depends(get_db)):

    system_conf_query = db.query(models.System_conf).filter(
        models.System_conf.uid == ID)
    system_conf = system_conf_query.first()
    if system_conf == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"system_conf with id: {ID} does not exist")
    system_conf_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# GET A USER


@ router.get("/{ID}",)
# , current_system_conf: int = Depends(oauth2.get_current_system_conf)):
def get_system_conf(ID: int, db: Session = Depends(get_db)):

    system_conf_query = db.query(models.System_conf).filter(
        models.System_conf.uid == ID)
    system_conf = system_conf_query.first()

    if system_conf == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"system_conf with id: {ID} does not exist")
    return system_conf  # .__list__

# GET ALL SYSTEM_CONFS


@ router.get("/")
def get_all_system_confs(db: Session = Depends(get_db)):
    results = db.query(models.System_conf).all()

    return results


# UPDATE A USER
@ router.put("/{ID}")
def update_post(input: dict, ID: int, db: Session = Depends(get_db)):
    system_conf_query = db.query(models.System_conf).filter(
        models.System_conf.uid == ID)
    system_conf = system_conf_query.first()

    if system_conf == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"system_conf with id: {ID} does not exist")

    system_conf_query.update(input, synchronize_session=False)
    db.commit()
    return system_conf_query.first()
