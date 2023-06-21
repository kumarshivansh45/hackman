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
    prefix="/fxn_configs",
    tags=['Fxn_configs']
)

# CREATE A USER


@router.post("/", status_code=status.HTTP_201_CREATED,)
def create_new_fxn_config(input: dict, db: Session = Depends(get_db)):

    new_fxn_config = models.Fxn_config(**input)
    db.add(new_fxn_config)
    db.commit()
    db.refresh(new_fxn_config)

    return new_fxn_config.__dict__


# DELETE A USER


@router.delete("/{ID}", status_code=status.HTTP_204_NO_CONTENT,)
def delete_a_fxn_config(ID: int, db: Session = Depends(get_db)):

    fxn_config_query = db.query(models.Fxn_config).filter(
        models.Fxn_config.uid == ID)
    fxn_config = fxn_config_query.first()
    if fxn_config == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"fxn_config with id: {ID} does not exist")
    fxn_config_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# GET A USER


@ router.get("/{ID}",)
# , current_fxn_config: int = Depends(oauth2.get_current_fxn_config)):
def get_fxn_config(ID: int, db: Session = Depends(get_db)):

    fxn_config_query = db.query(models.Fxn_config).filter(
        models.Fxn_config.uid == ID)
    fxn_config = fxn_config_query.first()

    if fxn_config == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"fxn_config with id: {ID} does not exist")
    return fxn_config  # .__list__

# GET ALL FXN_CONFIGS


@ router.get("/")
def get_all_fxn_configs(db: Session = Depends(get_db)):
    results = db.query(models.Fxn_config).all()

    return results


# UPDATE A USER
@ router.put("/{ID}")
def update_post(input: dict, ID: int, db: Session = Depends(get_db)):
    fxn_config_query = db.query(models.Fxn_config).filter(
        models.Fxn_config.uid == ID)
    fxn_config = fxn_config_query.first()

    if fxn_config == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"fxn_config with id: {ID} does not exist")

    fxn_config_query.update(input, synchronize_session=False)
    db.commit()
    return fxn_config_query.first()
