from enum import unique
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, false
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from utils import rand_key
from database import Base


class Captchas_data(Base):
    __tablename__ = "captcha_data"
    uid = Column(Integer, primary_key=True, nullable=False )
    token_number = Column(String(40), unique=True, nullable=False )
    valid_time = Column(String(20), unique=False, nullable=False)
    reason_api = Column(String(100), unique=False, nullable=False)
    mac_ip_address = Column(String(200), unique=False, nullable=False)

class User_data(Base):
    __tablename__ = "user_data"
    uid =  Column(Integer, primary_key=True, nullable=False )
    phone =  Column(String(20), unique=True, nullable=False )
    email =  Column(String(100), unique=True, nullable=False )
    profile_pic = Column(String(20000), unique=False, nullable=True)
    adhaar_verified_or_not = Column(Boolean, nullable=False,default=False)
    google_login_code = Column(String(200), unique=True, nullable=True)
    apple_login_code = Column(String(200), unique=True, nullable=True)
    score = Column(String(100), unique=False, nullable=False , default = '0')
    user_group = Column(String(100), unique=False, nullable=True)
    password_hash = Column(String(500), unique=False, nullable=False)
    
class Permissions_data(Base):
    __tablename__ = "Permissions_data"
    uid =  Column(Integer, primary_key=True, nullable=False )
    name = Column(String(100), unique=True, nullable=False)
    create = Column(String(500), unique=False, nullable=False)
    read = Column(String(500), unique=False, nullable=False)
    update = Column(String(500), unique=False, nullable=False)
    delete = Column(String(500), unique=False, nullable=False)
    execute = Column(String(500), unique=False, nullable=False)
    tfa = Column(String(500), unique=False, nullable=False)
    captcha = Column(String(500), unique=False, nullable=False) # mandatory for all open api's
    
class Products_data(Base):
    __tablename__ = "Products_data"
    uid =  Column(Integer, primary_key=True, nullable=False )
    company_name = Column(String(100),unique=False,nullable=False)
    product_name = Column(String(200),unique=False,nullable=False)
    company_cin = Column(String(100),unique=False,nullable=False)
    category = Column(String(100),unique=False,nullable=False)
    meta_data = Column(String(50000), unique=False,nullable=True)
    image = Column(String(50000), unique=False,nullable=True)
    expiration_duration_in_days = Column(Integer,unique=False,nullable=True)

# class Product_items_data(Base):
#     __tablename__ =     
# class Data_conf(Base):
#     __tablename__ = "data_conf"
#     uid = Column(Integer, primary_key=True, nullable=False)
#     table_name = Column(String, nullable=False, unique=True)
#     data_name = Column(String, nullable=False, unique=False)
#     stored_at = Column(String, nullable=False, unique=False)
#     encrypted_on_device = Column(String, nullable=False, unique=False)
#     encrypted_on_server = Column(String, nullable=False, unique=False)
#     encrypted_while_transmission = Column(String, nullable=False, unique=False)
#     compressed_on_device = Column(String, nullable=False, unique=False)
#     compressed_on_server = Column(String, nullable=False, unique=False)
#     compressed_on_transmission = Column(String, nullable=False, unique=False)
#     Who_can_read = Column(String, nullable=False, unique=False)
#     Who_can_write = Column(String, nullable=False, unique=False)
#     Who_can_update = Column(String, nullable=False, unique=False)
#     who_can_delete = Column(String, nullable=False, unique=False)
#     # created_updated_date =  NEED TO SET WITH IST
#     create_updated_request_date = Column(String, nullable=False, unique=False)
#     backed_up_or_not = Column(String, nullable=False, unique=False)
#     expirey_duration = Column(String, nullable=False, unique=False)
#     # schema before database query in seperate folder , might be unnecessary
#     max_length_charecter = Column(String, nullable=False, unique=False)
#     user_specific = Column(String, nullable=False, unique=False)
#     comments = Column(String, nullable=True, unique=False)


# class Language(Base):
#     __tablename__ = "language"
#     uid = Column(Integer, primary_key=True, nullable=False)
#     alias = Column(String, unique=True, nullable=False)
#     english = Column(String, unique=False, nullable=True)
#     kannada = Column(String, unique=False, nullable=True)
#     details = Column(String, unique=False, nullable=True)


# class Messages(Base):
#     __tablename__ = "messages"
#     uid = Column(Integer, primary_key=True, nullable=False)
#     alias = Column(String, unique=True, nullable=False)
#     content = Column(String, unique=False, nullable=True)
#     details = Column(String, unique=False, nullable=True)


# class Articles(Base):
#     __tablename__ = "articles"
#     uid = Column(Integer, primary_key=True, nullable=False)
#     alias = Column(String, unique=True, nullable=False)
#     content = Column(String, unique=False, nullable=True)
#     viewed = Column(String, unique=False, nullable=True)
#     expanded = Column(String, unique=False, nullable=True)
#     full_read = Column(String, unique=False, nullable=True)
#     details = Column(String, unique=False, nullable=True)


# class Surveys(Base):
#     __tablename__ = "surveys"
#     uid = Column(Integer, primary_key=True, nullable=False)
#     alias = Column(String, unique=True, nullable=False)
#     viewed = Column(String, unique=False, nullable=True)
#     answered = Column(String, unique=False, nullable=True)
#     skipped = Column(String, unique=False, nullable=True)
#     pushable_or_not = Column(String, unique=False, nullable=True)
#     content = Column(String, unique=False, nullable=True)
#     details = Column(String, unique=False, nullable=True)


# class Ads(Base):
#     __tablename__ = "ads"
#     uid = Column(Integer, primary_key=True, nullable=False)
#     alias = Column(String, unique=True, nullable=False)
#     viewed = Column(String, unique=False, nullable=True)
#     clicked = Column(String, unique=False, nullable=True)
#     skipped = Column(String, unique=False, nullable=True)
#     pushable_or_not = Column(String, unique=False, nullable=True)
#     content = Column(String, unique=False, nullable=True)
#     details = Column(String, unique=False, nullable=True)


# class Function_conf(Base):
#     __tablename__ = "function_conf"
#     uid = Column(Integer, primary_key=True, nullable=False)
#     fxn_name = Column(String, unique=True, nullable=False)
#     exe_permission = Column(String, nullable=False, unique=False)
#     # Request n response body schema in a seperate folder
#     # code,message,handling_fxn
#     error_codes_messages = Column(String, nullable=False, unique=False)
#     alert_functions = Column(String, nullable=False,
#                              unique=False)  # when done send sms,etc
#     public_or_private = Column(
#         String, nullable=False, unique=False)  # for api's
#     rate_limit = Column(String, nullable=False, unique=False)
#     jail_time = Column(String, nullable=False, unique=False)
#     max_calls_allowed = Column(String, nullable=False, unique=False)
#     # immidiate,background,scheduled
#     priority_class = Column(String, nullable=False, unique=False)
#     comments = Column(String, nullable=False, unique=False)


# class Forensics(Base):
#     __tablename__ = "forensics"
#     uid = Column(Integer, primary_key=True, nullable=False)
#     fxn_name = Column(String, unique=True, nullable=False)
#     exe_by = Column(String, nullable=False, unique=False)
#     # executed time in IST
#     inputs = Column(String, nullable=False, unique=False)
#     output = Column(String, nullable=False, unique=False)
#     requested_time = Column(String, nullable=False, unique=False)
#     # ip address,mac address
#     security_data = Column(String, nullable=False, unique=False)


# class System_conf(Base):
#     __tablename__ = "system_conf"
#     uid = Column(Integer, primary_key=True, nullable=False)
#     key = Column(String, unique=True, nullable=False)
#     value = Column(String, unique=False, nullable=False)
#     comments = Column(String, nullable=False, unique=False)


# class Universal_app_data(Base):
#     __tablename__ = "universal app data"
#     uid = Column(Integer, primary_key=True, nullable=False)
#     key = Column(String, unique=True, nullable=False)
#     value = Column(String, unique=False, nullable=True)
#     comments = Column(String, nullable=True, unique=False)


# class User(Base):
#     __tablename__ = "users"
#     uid = Column(Integer, primary_key=True, nullable=False)
#     user_name = Column(String, nullable=False,
#                        unique=True)
#     email = Column(String, nullable=False, unique=True)
#     phone = Column(String, nullable=False, unique=True)
#     password = Column(String, nullable=False, unique=False)
#     details = Column(String, nullable=True, unique=False)
#     group = Column(String, nullable=False, unique=False, server_default="user")
#     jwt = Column(String, nullable=True, unique=False)
#     journey = Column(String, nullable=True, unique=False)
#     language = Column(String, nullable=False, unique=False)
# # change nullables to true , idiot


# class Buses(Base):
#     __tablename__ = "buses"
#     uid = Column(Integer, primary_key=True, nullable=False)
#     alias = Column(String, nullable=False, unique=True)
#     num_plate = Column(String, nullable=False, unique=True)
#     details = Column(String, nullable=True, unique=False)


# class Stoppages(Base):
#     __tablename__ = "stoppages"
#     uid = Column(Integer, primary_key=True, nullable=False)
#     alias = Column(String, nullable=False, unique=True)
#     coordinates = Column(String, nullable=True, unique=False)
#     details = Column(String, nullable=True, unique=False)


# class Trip_routes(Base):
#     __tablename__ = "trip_routes"
#     uid = Column(Integer, primary_key=True, nullable=False)
#     alias = Column(String, nullable=False, unique=True)
#     route = Column(String, nullable=True, unique=False)
#     timestamps = Column(String, nullable=True, unique=False)
#     details = Column(String, nullable=True, unique=False)


# class Journey(Base):
#     __tablename__ = "journey"
#     uid = Column(Integer, primary_key=True, nullable=False)
#     alias = Column(String, nullable=False, unique=True)
#     # driver,conductor,passenger
#     passengers = Column(String, nullable=True, unique=False)
#     journey_date = Column(String, nullable=True, unique=False)
#     boarding_stop = Column(String, nullable=True, unique=False)
#     endingColumn = Column(String, nullable=True, unique=False)
#     transaction_id = Column(String, nullable=True, unique=False)
#     fare = Column(String, nullable=True, unique=False)
#     other_details = Column(String, nullable=False, unique=True)
#     details = Column(String, nullable=True, unique=False)


# class Tracking(Base):
#     __tablename__ = "tracking"
#     uid = Column(Integer, primary_key=True, nullable=False)
#     journey = Column(String, ForeignKey(
#         "journey.alias", ondelete='CASCADE'), nullable=False, unique=True)
#     stops_crossed = Column(String, nullable=True, unique=False)
#     time_delay = Column(String, nullable=True, unique=False)
#     distance_from_last_stop = Column(String, nullable=True, unique=False)


# # class Post(Base):
# #     __tablename__ = "posts"

# #     id = Column(Integer, primary_key=True, nullable=False)
# #     title = Column(String, nullable=False)
# #     content = Column(String, nullable=False)
# #     published = Column(Boolean, server_default='TRUE', nullable=False)
# #     created_at = Column(TIMESTAMP(timezone=True),
# #                         nullable=False, server_default=text('now()'))
# #     owner_id = Column(Integer, ForeignKey(
# #         "users.id", ondelete="CASCADE"), nullable=False)

# #     owner = relationship("User")


# # class conduc
# # class VarTokens(Base):
# #     __tablename__ = "var_tokens"
# #     id = Column(Integer, primary_key=True, nullable=False)
# #     user_id = Column(Integer, ForeignKey(
# #         "users.id", ondelete="CASCADE"), primary_key=True)
# #     captcha = Column(String, nullable=False, unique=True,
# #                      server_default=rand_key(7))
# #     jwt = Column(String, nullable=True, unique=True)
# #     captcha_time = Column(TIMESTAMP(timezone=True),
# #                           nullable=False, server_default=text('now()'))


# # class ServeraVsr(Base):
# #     __tablename__ = "server_var"
# #     id = Column(Integer, primary_key=True, nullable=False)
# #     key = Column(String, unique=True, nullable=False)
# #     value = Column(String, unique=False, nullable=True)

# # class Vote(Base):
# #     __tablename__ = "votes"
# #     user_id = Column(Integer, ForeignKey(
# #         "users.id", ondelete="CASCADE"), primary_key=True)
# #     post_id = Column(Integer, ForeignKey(
# #         "posts.id", ondelete="CASCADE"), primary_key=True)
