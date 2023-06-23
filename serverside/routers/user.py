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
@router.post("/create_user", status_code=status.HTTP_201_CREATED,)
def create_new_user(input: dict, db: Session = Depends(get_db)):
    # phone =  Column(String(20), unique=True, nullable=False )
    # email =  Column(String(100), unique=True, nullable=False )
    # profile_pic = Column(String(20000), unique=False, nullable=True)
    # adhaar_verified_or_not = Column(Boolean, nullable=False,default=False)
    # google_login_code = Column(String(200), unique=True, nullable=True)
    # apple_login_code = Column(String(200), unique=True, nullable=True)
    # score = Column(String(100), unique=False, nullable=False)
    # user_group = Column(String(100), unique=False, nullable=True)
    # password_hash = Column(String(500), unique=False, nullable=False)
    user_phone = input["phone"]
    user_email = input["email"]
    user_group = input["user_group"]
    user_passwd = input["passwd"]
    user_passwd = utils.hash(user_passwd)
    # user_cap_token = input["token_number"]
    # {"phone":"7023756123","email":"kumar.shivansh45@gmail.com","user_group":"admin","passwd":"Masterpass1.","token_number":""}

    if utils.validate_captcha_token(input)!={"yay":"success"}:
        return {"oops":"captcha token didnt match"}
        # check strong password
    new_user = models.User_data(
        phone=user_phone, email=user_email, user_group=user_group,password_hash=user_passwd)
    # print(">>>>>>>>>>>>>", input, type(input))
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except :
        return {"oops":"something went wrong , maybe a similar email/phone already exists"}


    return {"yay":"user added successfully"}
    
        

# # DELETE A USER


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT,)
def delete_a_user(ID: int, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):

    user_query = db.query(models.User).filter(models.User.uid == ID)
    user = user_query.first()
    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id: {ID} does not exist")
    user_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# # GET A USER


# @ router.get("/{ID}",)
# # , current_user: int = Depends(oauth2.get_current_user)):
# def get_user(ID: int, db: Session = Depends(get_db)):

#     user_query = db.query(models.User).filter(
#         models.User.uid == ID)
#     user = user_query.first()

#     if user == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"user with id: {ID} does not exist")
#     return user  # .__list__

# # GET ALL USERS


# @ router.get("/")
# def get_all_users(db: Session = Depends(get_db)):
#     results = db.query(models.User).all()

#     return results


# # UPDATE A USER
# @ router.put("/{ID}")
# def update_post(input: dict, ID: int, db: Session = Depends(get_db)):
#     user_query = db.query(models.User).filter(
#         models.User.uid == ID)
#     user = user_query.first()

#     if user == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"user with id: {ID} does not exist")
#     if (input["conf_password"] == input["password"]):
#         value = input.pop("conf_password")

#         user_query.update(input, synchronize_session=False)
#         db.commit()
#         return user_query.first()

#     else:
#         raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED,
#                             detail=f"passwd & conf_passwd dont match")
