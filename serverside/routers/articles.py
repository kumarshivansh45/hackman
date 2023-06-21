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
    prefix="/articles",
    tags=['Articles']
)

# CREATE A USER


@router.post("/", status_code=status.HTTP_201_CREATED,)
def create_new_article(input: dict, db: Session = Depends(get_db)):

    new_article = models.Article(**input)
    db.add(new_article)
    db.commit()
    db.refresh(new_article)

    return new_article.__dict__


# DELETE A USER


@router.delete("/{ID}", status_code=status.HTTP_204_NO_CONTENT,)
def delete_a_article(ID: int, db: Session = Depends(get_db)):

    article_query = db.query(models.Article).filter(
        models.Article.uid == ID)
    article = article_query.first()
    if article == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"article with id: {ID} does not exist")
    article_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# GET A USER


@ router.get("/{ID}",)
# , current_article: int = Depends(oauth2.get_current_article)):
def get_article(ID: int, db: Session = Depends(get_db)):

    article_query = db.query(models.Article).filter(
        models.Article.uid == ID)
    article = article_query.first()

    if article == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"article with id: {ID} does not exist")
    return article  # .__list__

# GET ALL ARTICLES


@ router.get("/")
def get_all_articles(db: Session = Depends(get_db)):
    results = db.query(models.Article).all()

    return results


# UPDATE A USER
@ router.put("/{ID}")
def update_post(input: dict, ID: int, db: Session = Depends(get_db)):
    article_query = db.query(models.Article).filter(
        models.Article.uid == ID)
    article = article_query.first()

    if article == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"article with id: {ID} does not exist")

    article_query.update(input, synchronize_session=False)
    db.commit()
    return article_query.first()
