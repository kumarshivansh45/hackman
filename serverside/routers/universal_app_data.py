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
    prefix="/universal_app_datas",
    tags=['Universal_app_datas']
)

# CREATE A USER


@router.post("/", status_code=status.HTTP_201_CREATED,)
def create_new_universal_app_data(input: dict, db: Session = Depends(get_db)):

    new_universal_app_data = models.Language(**input)
    db.add(new_universal_app_data)
    db.commit()
    db.refresh(new_universal_app_data)

    return new_universal_app_data.__dict__


# DELETE A USER


@router.delete("/{ID}", status_code=status.HTTP_204_NO_CONTENT,)
def delete_a_universal_app_data(ID: int, db: Session = Depends(get_db)):

    universal_app_data_query = db.query(models.Language).filter(
        models.Language.uid == ID)
    universal_app_data = universal_app_data_query.first()
    if universal_app_data == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"universal_app_data with id: {ID} does not exist")
    universal_app_data_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# GET A USER


@ router.get("/{ID}",)
# , current_universal_app_data: int = Depends(oauth2.get_current_universal_app_data)):
def get_universal_app_data(ID: int, db: Session = Depends(get_db)):

    universal_app_data_query = db.query(models.Language).filter(
        models.Language.uid == ID)
    universal_app_data = universal_app_data_query.first()

    if universal_app_data == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"universal_app_data with id: {ID} does not exist")
    return universal_app_data  # .__list__

# GET ALL UNIVERSAL_APP_DATAS


@ router.get("/")
def get_all_universal_app_datas(db: Session = Depends(get_db)):
    results = db.query(models.Language).all()

    return results


# UPDATE A USER
@ router.put("/{ID}")
def update_post(input: dict, ID: int, db: Session = Depends(get_db)):
    universal_app_data_query = db.query(models.Language).filter(
        models.Language.uid == ID)
    universal_app_data = universal_app_data_query.first()

    if universal_app_data == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"universal_app_data with id: {ID} does not exist")

    universal_app_data_query.update(input, synchronize_session=False)
    db.commit()
    return universal_app_data_query.first()
