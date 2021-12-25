from rave_python import Rave
from flask import Flask, request
import json
import sys
import pyrebase

app = Flask(__name__)

firebaseConfig = {
    'apiKey': "AIzaSyDySGSLHwwPI_ouMYFaSlG53YEz_U5VVH4",
    'authDomain': "splishpay-tga.firebaseapp.com",
    'projectId': "splishpay-tga",
    'storageBucket': "splishpay-tga.appspot.com",
    'messagingSenderId': "989782550449",
    'appId': "1:989782550449:web:ce0df59b2fddf4d7d8ff90",
    'measurementId': "G-1TTHTEQG8M"}

firebase = pyrebase.initialize_app(firebaseConfig)
mAuth = firebase.auth()

# storage=firebase.storage()


@app.route('/pay', methods=['POST'])
def pay():
    mRes = request.json

    print(type(mRes))

    rave = Rave("FLWPUBK_TEST-9b7e67b3f92743577a71e213ae831c30-X",
                "FLWSECK_TEST-d7c930ee491d6e2664ec55eba9d1082d-X", usingEnv=False)

    # x = '{ "cardno" : "5531886652142950", "cvv" : "564", "currency" : "NGN", "country" : "NG", "expirymonth" : "09", "expiryyear" : "32", "amount" : "1000", "email" : "pr.mayami@gmail.com", "phonenumber" : "09039712085", "firstname" : "Joe", "lastname" : "Mayami"}'

    r = json.dumps(mRes)
    payload = json.loads(r)
    res = rave.Card.charge(payload)

    return str(res['txRef'])


@app.route('/login', method=['POST'])
def login():
    try:
        mEmail = "pr.mayami@gmail.com"
        mPassword = "footBall@2020"
        res = mAuth.sign_in_with_email_and_password(mEmail, mPassword)
    except Exception as e:
        print("An error occured: " + str(e))

        return e

    return res


@app.route('/signup', method=['POST'])
def signup():
    try:
        mEmail = "pr.mayami@gmail.com"
        mPassword = "footBall@2020"
        res = mAuth.create_user_with_email_and_password(mEmail, mPassword)
    except Exception as e:
        print("An error occured: " + str(e))

        return e

    return res
