from pydantic import BaseModel, EmailStr, constr
from datetime import datetime
from typing import Optional

from pydantic.types import conint


# class PostBase(BaseModel):
#     title: str
#     content: str
#     published: bool = True


# class PostCreate(PostBase):
#     pass


# class UserOut(BaseModel):
#     id: int
#     email: EmailStr
#     created_at: datetime

#     class Config:
#         orm_mode = True


# class Post(PostBase):
#     id: int
#     created_at: datetime
#     owner_id: int
#     owner: UserOut

#     class Config:
#         orm_mode = True


# class PostOut(BaseModel):
#     Post: Post
#     votes: int

#     class Config:
#         orm_mode = True

class Data_Conf_input(BaseModel):
    uid: int
    table_name: str
    data_name: str
    stored_at: str
    encrypted_on_device: str
    encrypted_on_server: str
    encrypted_while_transmission: str
    compressed_on_device: str
    compressed_on_server: str
    compressed_on_transmission: str
    Who_can_read: str
    Who_can_write: str
    Who_can_update: str
    who_can_delete: str
    create_updated_request_date: str
    backed_up_or_not: str
    expirey_duration: str
    max_length_charecter: str
    user_specific: str
    comments: str


class Language_input(BaseModel):

    uid: int
    alias: str
    english: str
    kannada: str
    details: str


class Message_input(BaseModel):

    uid: int
    alias: str
    content: str
    details: str


class Articles_input(BaseModel):
    uid: int
    alias: str
    content: str
    viewed: str
    expanded: str
    full_read: str
    details: str


class Surveys_input(BaseModel):
    uid: int
    alias: str
    viewed: str
    answered: str
    skipped: str
    pushable_or_not: str
    content: str
    details: str


class Ads_input(BaseModel):
    uid: int
    alias: str
    viewed: str
    clicked: str
    skipped: str
    pushable_or_not: str
    content: str
    details: str


class Function_conf_input(BaseModel):
    uid: int
    fxn_name: str
    exe_permission: str
    error_codes_messages: str
    alert_functions: str
    public_or_private: str
    rate_limit: str
    jail_time: str
    max_calls_allowed: str
    # immidiate,background,scheduled
    priority_class: str
    comments: str


class Forensics_input(BaseModel):
    uid: int
    fxn_name: str
    exe_by: str
    # executed time in IST
    inputs: str
    output: str
    requested_time: str
    # ip address,mac address
    security_data: str


class System_conf_input(BaseModel):

    uid: int
    key: str
    value: str
    comments: str


class Universal_app_data_input(BaseModel):
    uid: int
    key: str
    value: str
    comments: str


class UserCreateInput(BaseModel):
    name: Optional[constr(max_length=10)]
    email: Optional[constr(max_length=100)]
    phone: Optional[constr(max_length=100)]
    password: Optional[constr(max_length=100)]
    conf_password: Optional[constr(max_length=100)]
    details: Optional[constr(max_length=100)]
    group: Optional[constr(max_length=100)]
    jwt: Optional[constr(max_length=100)]
    journey: Optional[constr(max_length=100)]
    language: Optional[constr(max_length=100)]

    class Config:
        orm_mode = True


class UserCreateOutput(BaseModel):
    uid: Optional[int]
    name: Optional[constr(max_length=100)]
    email: Optional[constr(max_length=100)]
    phone: Optional[constr(max_length=100)]
    password: Optional[constr(max_length=100)]
    details: Optional[constr(max_length=100)]
    group: Optional[constr(max_length=100)]
    jwt: Optional[constr(max_length=100)]
    journey: Optional[constr(max_length=100)]
    language: Optional[constr(max_length=100)]

    class Config:
        orm_mode = True


class Buses_input(BaseModel):
    uid: int
    alias: str
    num_plate: str
    details: str


class Stoppages_input(BaseModel):
    uid: int
    alias: str
    coordinates: str
    details: str


class Trip_routes_input(BaseModel):
    uid: int
    alias: str
    route: str
    timestamps: str
    details: str


class Journey_input(BaseModel):
    uid: int
    alias: str
    # driver,conductor,passenger
    passengers: str
    journey_date: str
    boarding_stop: str
    endingColumn: str
    transaction_id: str
    fare: str
    other_details: str
    details: str


class Tracking_input(BaseModel):
    uid: int
    journey: str
    stops_crossed: str
    time_delay: str
    distance_from_last_stop: str
# class UserLogin(BaseModel):
#     phone: str
#     password: str

#     class Token(BaseModel):
#         access_token: str
#         token_type: str

#     class TokenData(BaseModel):
#         id: Optional[str] = None

    # class Vote(BaseModel):
    #     post_id: int
    #     dir: conint(le=1)
