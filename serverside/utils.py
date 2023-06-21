# IMPORTS
import os
import base64
import random
import string
from PIL import Image
import io
import json
from datetime import datetime, timedelta
import urllib
# MAIL dependency packages
from email import message
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from captcha.image import ImageCaptcha
# RSA dependency packages
import rsa
# AES dependency packages
from secrets import token_bytes
from Crypto.Cipher import AES
import hashlib
# PASSWORD_HASHING dependency packages
from passlib.context import CryptContext
from rsa import PrivateKey, encrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


    


def time_now():
    return str(datetime.now())


def string2time(x):
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')


def bytes2imageObject(bytes):
    imm = Image.open(io.BytesIO(bytes))
    return imm


def hexbits2b64string(x):
    return base64.b64encode(x).decode('ascii')


def b64string2hexbits(x):
    return (base64.b64decode(x))


def mail(sendtoList, content, subject="do NOT reply : system generated mail"):
    # Credentials
    username = 'teambitwiz@gmail.com'
    password = 'oihzszewghdscxkf'

    # note - this smtp config worked for me, I found it googling around, you may have to tweak the # (587) to get yours to work
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(username, password)

    # app password for this device ckeyexkwnflrpjbb
    from_address = "teambitwiz@gmail.com"
    for x in sendtoList:
        to_address = x

        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = from_address
        msg['To'] = to_address

        # Create the message (HTML).
        text = content

        # Record the MIME type - text/html.
        part1 = MIMEText(text)
        # Attach parts into message container
        msg.attach(part1)

        # Sending the email
        server.sendmail(from_address, to_address, msg.as_string())
    server.quit()
# mail(['kumar.shivansh45@gmail.com'],"hi , mail sending successful")


def randomAlphaNumeric(size):
    S = size  # number of characters in the string.
    # call random.choices() string module to find the string in Uppercase + numeric data.
    ran = ''.join(random.choices(string.ascii_uppercase +
                  string.ascii_lowercase + string.digits, k=S))
    # print the random data
    return (str(ran))


def hash(password: str):
    return pwd_context.hash(password)


def check_internet():
    try:
        urllib.request.urlopen('https://google.com/', timeout=3)
        return True
    except:
        return False


def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# RECONFIGURATION OF SMS MODULE
def sms(number, message):  # fast2sms.com
    URL = "https://www.fast2sms.com/dev/bulkV2"

    HEADERS = {
        "authorization": "G7Fw6WkjPgtW9qZQzLxXn2ENX2ThlDdMM9TsOc8FNavC1nJAJKKI9VWf8IVD"
    }

    DATA = {
        "route": "q",
        "message": message,
        "language": "english",
        "flash": 0,
        "numbers": number,
    }

    r = requests.post(url=URL, headers=HEADERS, data=DATA)
    return (r.status_code)


def captcha(captcha_text):
    # Create an image instance of the given size
    image = ImageCaptcha(width=200, height=90)
    # generate the image of the given text
    data = image.generate(captcha_text)
    data = data.read()
    data = hexbits2b64string(data)
    # print(data)
    return data


# captcha('shiva')


def rand_key(size):  # FOR GENERATING RANDOM KEYS

    x = ''.join(random.choice(string.ascii_uppercase +
                string.ascii_lowercase + string.digits) for _ in range(size))
    return (x)


temp_key = b"\x0e\x8a\xc5\xa1\xa2\x8c\x99\x98\xdc\xc9\xe1\xdd\x8e\xf2[\x83"


def pass_2_key(passwd):
    hashed_string = hashlib.sha256(passwd.encode('utf-8')).hexdigest()
    return (hashed_string)


def aes_encrypt(message, key):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(message.encode('ascii'))
    return {'ciphertext': ciphertext, 'tag': tag, 'nonce': nonce}


def aes_decrypt(ciphertext, tag, key, nonce):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False

# new_key='a2Df4Ghtki32TY33'
# new_key = bytes(new_key,'utf-8')
# print(new_key)
# message = "i love you dhanyashree"
# hash = aes_encrypt(message,key=new_key)
# print(hash)
# print(aes_decrypt(hash['ciphertext'], hash['tag'], new_key, hash['nonce']))


def RSAgenerateKeys():
    (publicKey, privateKey) = rsa.newkeys(1024)
    with open('./keys/publicKey.pem', 'wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
    with open('./keys/privateKey.pem', 'wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))


def RSAloadKeys():
    with open('./keys/publicKey.pem', 'rb') as p:
        publicKey = rsa.PublicKey.load_pkcs1(p.read())
    with open('./keys/privateKey.pem', 'rb') as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())
    return privateKey, publicKey


def RSAencrypt(message, key):
    return rsa.encrypt(message.encode('ascii'), key)


def RSAdecrypt(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')
    except:
        return False


def RSAsign(message, key):
    return rsa.sign(message.encode('ascii'), key, 'SHA-1')


def RSAverify(message, signature, key):
    try:
        return rsa.verify(message.encode('ascii'), signature, key) == 'SHA-1'
    except:
        return False

# dict = aes_encrypt("dhanyashree has a solid figure", temp_key)
# print(aes_decrypt(dict['ciphertext'], dict['tag'], temp_key, dict['nonce']))


# RSAgenerateKeys()
# privateKey,publicKey  = RSAloadKeys()
# message = input('Write your message here:')
# ciphertext = RSAencrypt(message, publicKey)
# print(f"ciphertext : {ciphertext}")
# plaintext = RSAdecrypt(ciphertext, privateKey)
# print(f"plaintext:{plaintext}")
# signature = RSAsign(message,privateKey)
# print(f"signature : {signature}")
# if RSAverify(plaintext,signature,publicKey):
#     print("successfully verified signature")
# else:
#     print("signature didnt match")
#


# print(str(datetime.now()))
