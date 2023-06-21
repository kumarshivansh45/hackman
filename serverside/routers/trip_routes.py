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
    prefix="/trip_routes",
    tags=['Trip_routes']
)

# CREATE A USER


@router.post("/", status_code=status.HTTP_201_CREATED,)
def create_new_trip_route(input: dict, db: Session = Depends(get_db)):

    new_trip_route = models.Trip_route(**input)
    db.add(new_trip_route)
    db.commit()
    db.refresh(new_trip_route)

    return new_trip_route.__dict__


# DELETE A USER


@router.delete("/{ID}", status_code=status.HTTP_204_NO_CONTENT,)
def delete_a_trip_route(ID: int, db: Session = Depends(get_db)):

    trip_route_query = db.query(models.Trip_route).filter(
        models.Trip_route.uid == ID)
    trip_route = trip_route_query.first()
    if trip_route == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"trip_route with id: {ID} does not exist")
    trip_route_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# GET A USER


@ router.get("/{ID}",)
# , current_trip_route: int = Depends(oauth2.get_current_trip_route)):
def get_trip_route(ID: int, db: Session = Depends(get_db)):

    trip_route_query = db.query(models.Trip_route).filter(
        models.Trip_route.uid == ID)
    trip_route = trip_route_query.first()

    if trip_route == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"trip_route with id: {ID} does not exist")
    return trip_route  # .__list__

# GET ALL TRIP_ROUTES


@ router.get("/")
def get_all_trip_routes(db: Session = Depends(get_db)):
    results = db.query(models.Trip_route).all()

    return results


# UPDATE A USER
@ router.put("/{ID}")
def update_post(input: dict, ID: int, db: Session = Depends(get_db)):
    trip_route_query = db.query(models.Trip_route).filter(
        models.Trip_route.uid == ID)
    trip_route = trip_route_query.first()

    if trip_route == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"trip_route with id: {ID} does not exist")

    trip_route_query.update(input, synchronize_session=False)
    db.commit()
    return trip_route_query.first()
