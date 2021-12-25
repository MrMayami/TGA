from rave_python import Rave
from flask import Flask, request
import json
import sys

app = Flask(__name__)


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
