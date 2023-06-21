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
    prefix="/ads",
    tags=['Ads']
)

# CREATE A USER


@router.post("/", status_code=status.HTTP_201_CREATED,)
def create_new_ad(input: dict, db: Session = Depends(get_db)):

    new_ad = models.Ad(**input)
    db.add(new_ad)
    db.commit()
    db.refresh(new_ad)

    return new_ad.__dict__


# DELETE A USER


@router.delete("/{ID}", status_code=status.HTTP_204_NO_CONTENT,)
def delete_a_ad(ID: int, db: Session = Depends(get_db)):

    ad_query = db.query(models.Ad).filter(
        models.Ad.uid == ID)
    ad = ad_query.first()
    if ad == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"ad with id: {ID} does not exist")
    ad_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# GET A USER


@ router.get("/{ID}",)
# , current_ad: int = Depends(oauth2.get_current_ad)):
def get_ad(ID: int, db: Session = Depends(get_db)):

    ad_query = db.query(models.Ad).filter(
        models.Ad.uid == ID)
    ad = ad_query.first()

    if ad == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"ad with id: {ID} does not exist")
    return ad  # .__list__

# GET ALL ADS


@ router.get("/")
def get_all_ads(db: Session = Depends(get_db)):
    results = db.query(models.Ad).all()

    return results


# UPDATE A USER
@ router.put("/{ID}")
def update_post(input: dict, ID: int, db: Session = Depends(get_db)):
    ad_query = db.query(models.Ad).filter(
        models.Ad.uid == ID)
    ad = ad_query.first()

    if ad == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"ad with id: {ID} does not exist")

    ad_query.update(input, synchronize_session=False)
    db.commit()
    return ad_query.first()
