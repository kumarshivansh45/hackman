from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from config import Settings
import models
import oauth2
import schemas
import utils
import json
from database import get_db
import base64
from fastapi.encoders import jsonable_encoder
from datetime import datetime, timedelta

router = APIRouter(
    prefix="/captchas",
    tags=['Captchas']
)

settings = Settings()

# CREATE A USER


# @router.post("/", status_code=status.HTTP_201_CREATED,)
# def submit_captcha(input: dict, db: Session = Depends(get_db)):

#     # new_captcha = models.Captchas_data(**input)
#     print(">>>>>>>>>>>>>", input, type(input))

# db.add(new_ad)
# db.commit()
# db.refresh(new_ad)

# return new_ad.__dict__


# DELETE A USER


# @router.delete("/{ID}", status_code=status.HTTP_204_NO_CONTENT,)
# def delete_a_ad(ID: int, db: Session = Depends(get_db)):

#     ad_query = db.query(models.Ad).filter(
#         models.Ad.uid == ID)
#     ad = ad_query.first()
#     if ad == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"ad with id: {ID} does not exist")
#     ad_query.delete(synchronize_session=False)
#     db.commit()
#     return Response(status_code=status.HTTP_204_NO_CONTENT)


# GET A USER


# @ router.get("/{ID}",)
# # , current_ad: int = Depends(oauth2.get_current_ad)):
# def get_ad(ID: int, db: Session = Depends(get_db)):

#     ad_query = db.query(models.Ad).filter(
#         models.Ad.uid == ID)
#     ad = ad_query.first()

#     if ad == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"ad with id: {ID} does not exist")
#     return ad  # .__list__


# GET A CAPTCHA

@ router.post("/submit_cap", status_code=status.HTTP_201_CREATED)
def get_a_captcha(input: dict, db: Session = Depends(get_db)):
    # check if decrypt or not , if not decrypt alert admin and ignore
    captcha_response = input['captcha_response']
    hash_returned = input['hash_returned']
    hash_returned = json.loads(hash_returned)
    hash = json.loads(hash_returned['hash'])
    for k, v in hash.items():
        hash[k] = utils.b64string2hexbits(hash[k])
    key = settings.secret_key_aes
    key = bytes(key, 'ascii')
    text_recovered = (utils.aes_decrypt(
        hash['ciphertext'], hash['tag'], key, hash['nonce']))
    if not text_recovered:
        # report to admin
        return {'oops': 'something went wrong , this will be reported'}
    text_recovered = json.loads(text_recovered)
    random_text = text_recovered['random_text']
    # if captcha_reason valid , rate_limit:app id/ip/device-id non-suspecious , not changing
    old_mac_address = text_recovered['mac_address']
    old_mac_address = text_recovered['valid_reason']

    old_time_over = text_recovered["time_over"]
    # check time_over
    if (float((utils.string2time(old_time_over)-datetime.now()).total_seconds()) < 0):
        return {'oops': 'too late !'}

    # check if correct text or not
    if random_text != captcha_response:
        print(">>>>>>>>>", random_text, "!=", captcha_response)
        return {'oops': "incorrect captcha !"}
    # match device address/ip/app-address for change and rate-limits
    new_mac_address = 'ok'  # fetch from input
    new_valid_reason = 'valid'  # fetch from input
    # all ok create an instance

    new_time_over = str(
        datetime.now()+timedelta(minutes=int(settings.captcha_minutes)))
    token_number = utils.randomAlphaNumeric(32)
    results = db.query(models.Captchas_data).all()
    
    result_list = list()
    for result in results:
        result_list.append(str(result.token_number))
    while token_number in result_list:
        token_number = utils.randomAlphaNumeric(32)
    
    new_captcha_token = models.Captchas_data(
        token_number=token_number, valid_time=new_time_over, reason_api=new_valid_reason, mac_ip_address=new_mac_address)
    # print(">>>>>>>>>>>>>", input, type(input))

    db.add(new_captcha_token)
    db.commit()
    db.refresh(new_captcha_token)

    return new_captcha_token.__dict__


@ router.post("/get_cap")
def get_a_captcha(input: dict, db: Session = Depends(get_db)):
    # if captcha_reason valid , rate_limit:app id/ip/device-id non-suspecious
    # set valid-time
    mac_address = 'ok'  # fetch from input
    valid_reason = 'valid'  # fetch from input
    time_over = str(
        datetime.now()+timedelta(minutes=int(settings.captcha_minutes)))
    random_text = utils.randomAlphaNumeric(4)
    image_data = utils.captcha(random_text)
    final_text = {}
    final_text['random_text'] = random_text
    final_text['mac_address'] = mac_address
    final_text['valid_reason'] = valid_reason
    final_text["time_over"] = time_over
    final_text = json.dumps(final_text)
    key = settings.secret_key_aes
    key = bytes(key, 'ascii')
    hash = utils.aes_encrypt(final_text, key)
    for k, v in hash.items():
        hash[k] = utils.hexbits2b64string(hash[k])
    hash = json.dumps(hash)
    return_dict = {}
    return_dict['image'] = image_data
    return_dict['hash'] = hash
    return_dict = json.dumps(return_dict)
    return return_dict


# UPDATE A USER
# @ router.put("/{ID}")
# def update_post(input: dict, ID: int, db: Session = Depends(get_db)):
#     ad_query = db.query(models.Ad).filter(
#         models.Ad.uid == ID)
#     ad = ad_query.first()

#     if ad == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"ad with id: {ID} does not exist")

#     ad_query.update(input, synchronize_session=False)
#     db.commit()
#     return ad_query.first()
