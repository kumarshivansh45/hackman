# from PIL import Image
# import io
import requests
import base64
import io
import PIL.Image as Image
import json
import utils
from config import Settings
setting = Settings()

# # # Convert image to bytes
# # def image_to_bytes(image_path):
# #     with open(image_path, 'rb') as f:
# #         return f.read()

# # # Convert bytes to string
# # def bytes_to_string(byte_data):
# #     return byte_data.decode('latin-1')  # Use 'latin-1' encoding for arbitrary byte data

# # # Convert string to bytes
# # def string_to_bytes(string_data):
# #     return string_data.encode('latin-1')

# # # Convert bytes to image
# # def bytes_to_image(byte_data):
# #     image = Image.open(io.BytesIO(byte_data))
# #     return image

# # # Example usage
# # image_path = './cat.png'

# # # Convert image to bytes
# # image_bytes = image_to_bytes(image_path)
# # print("image bytes" , type(image_bytes),len(image_bytes))
# # # Convert bytes to string
# # byte_string = bytes_to_string(image_bytes)
# # print("byte_string" , type(byte_string),len(byte_string))

# # # Convert string to bytes
# # string_bytes = string_to_bytes(byte_string)
# # print("string_bytes" , type(string_bytes),len(string_bytes))

# # # Convert bytes to image
# # recovered_image = bytes_to_image(string_bytes)

# # # Display the recovered image
# # recovered_image.show()


# # importing the requests library
# # import requests ,shutil

# # # api-endpoint
# # URL = "http://127.0.0.1:8000/captchas/"

# # # location given here
# # location = "delhi technological university"

# # # defining a params dict for the parameters to be sent to the API
# # PARAMS = {'address':location}

# # # sending get request and saving the response as response object
# # r = requests.get(url = URL,stream=True)

# # # extracting data in json format
# # print(r.headers["content-type"])
# # with open('img.png', 'wb') as out_file:
# #     shutil.copyfileobj(r.raw, out_file)
# # del r

# # # Set the appropriate content types
# #     json_response.headers['Content-Type'] = 'application/json'
# #     json_response.headers['Image-Content-Type'] = 'image/jpeg'

# # hash = aes_encrypt("oh yeah", temp_key)
# # for k,v in hash.items():
# #     print(hash[k])
# #     hash[k]=base64.b64encode(v).decode('ascii')

# # for k,v in hash.items():
# #     hash[k]=(base64.b64decode(v))
# #     # hash[k]=str(hash[k],'ascii',errors=)
# #     print(hash[k])
# # print(aes_decrypt(hash['ciphertext'], hash['tag'], temp_key, hash['nonce']))

# # test = "hello"
# # print(0, test)
# # test = bytes(test, 'ascii')
# # print(1, test)
# # test = base64.b64encode(test)
# # print(2, test)
# # test = test.decode('ascii')
# # print(3, (test))
# # test = base64.b64decode(test)
# # print(4, test)
# # test = str(test,'ascii')
# # print(5, test)
# json_finally = "{\"image\": \"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\", \"hash\": \"{\\\"ciphertext\\\": \\\"JxygX2MqIyZaPtYC8dU9Wd0l1BogVvAKzPkB+GfXdOLgX+u5hWhkce4BlBE9nAds9SdfkEfbveWOK67Pt6sgdsLduRYxI7AaLlSZF84YV4+N3DrnSI7tJHGU7bvXVdkW2o+BiSssHRPo+r/ySoNsBQ==\\\", \\\"tag\\\": \\\"X4pz3NCmUL0oZx71mHlscQ==\\\", \\\"nonce\\\": \\\"RANCfpNgDG1+BIB8q54DqA==\\\"}\"}"
# print(type(json_finally))
# json_finally = json.loads(json_finally)
# print(type(json_finally))
# image = (utils.b64string2hexbits(json_finally['image']))
# image_print = image
# hash = json.loads(json_finally['hash'])
# for k, v in hash.items():
#     hash[k] = utils.b64string2hexbits(hash[k])
# key = setting.secret_key_aes
# key = bytes(key, 'ascii')
# text_recovered = (utils.aes_decrypt(
#     hash['ciphertext'], hash['tag'], key, hash['nonce']))
# text_recovered = json.loads(text_recovered)
# print(type(text_recovered))
# for k,v in text_recovered.items():
#     print(k, ":" ,v)

# # from byte_array import byte_data
# utils.bytes2imageObject(image_print).save('./captcha3.png')
# # # using tobytes data as raw for frombyte function

# # img = Image.frombytes("L", (200, 90), image)
# # img.show()
# # from datetime import datetime , timedelta
# # import time
# # t1 = datetime.now()
# # time.sleep(2)
# # t2 = datetime.now()
# # print(float((t1-t2).total_seconds()))
# # if float((t1-t2).total_seconds())<0:
# #     print("oh")


# # import requests

# # url = 'http://13.49.102.217/captchas/get_cap'
# # myobj = {'somekey': 'somevalue'}

# # x = requests.post(url, json = myobj)

# # print(x.text)


def login_attempt():
    url = "http://localhost:8000/login"
    head = {'Content-Type': 'application/x-www-form-urlencoded'}

    auth_info = {'username': '7023756123',
                 'password': 'Masterpass1.'
                 }

    # print(purl)
    # print(auth_info)
    # print(head)

    r = requests.post(url, auth_info, head)
    key = json.dumps(r.json())
    # print(key)
    key = json.loads(key)
    return key


def send_a_captcha():
    key = login_attempt()["access_token"]
    # print(type(key))
    head = {'Authorization':f'Bearer {key}'}
    # print(head)
    url = "http://localhost:8000/captchas/get_cap"
    # empty_json = {}
    # empty_json = json.dumps(empty_json)
    # print(">>>>>>>>>>>>>>>>>",type(empty_json))
    x1 = requests.post(url, json={},headers=head)
    # print(x.json())
    # data = x.text
    # print(x1.json())
    data = json.loads((x1.json()))
    hash = data["hash"]
    image = data["image"]
    hash = json.loads(data['hash'])
    for k, v in hash.items():
        hash[k] = utils.b64string2hexbits(hash[k])
    key = setting.secret_key_aes
    key = bytes(key, 'ascii')
    text_recovered = (utils.aes_decrypt(
        hash['ciphertext'], hash['tag'], key, hash['nonce']))
    text_recovered = json.loads(text_recovered)
    # print(type(text_recovered))
    captcha_val = text_recovered["random_text"]

    url2 = "http://localhost:8000/captchas/submit_cap"
    feed = (x1.json())
    # print(type(feed))
    # print(feed)
    x2 = requests.post(
        url2, json={"hash_returned": feed, "captcha_response": captcha_val})
    return (x2.json())

# print(type(json.dumps(send_a_captcha())))


def create_an_account():
    info = send_a_captcha()
    token_no = info["token_number"]
    # print(type(token_no))
    url = "http://localhost:8000/users/create_user"
    phone = input("enter phone ")
    email = input("enter email ")
    user_group = input("enter user_group ")
    passwd = input("enter password ")

    payload = {"phone": phone, "email": email, "user_group": user_group,
               "passwd": passwd, "token_number": token_no}
    # payload={"phone":"7023756123","email":"kumar.shivansh45@gmail.com","user_group":"admin","passwd":"Masterpass1.","token_number":""}

    payload = json.dumps(payload)
    # print(payload)
    x2 = requests.post(url, payload)
    print(x2.json())


# send_a_captcha()
# print(login_attempt())
# create_an_account()
print(login_attempt())