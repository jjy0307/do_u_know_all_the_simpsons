#페이지 구동이 되는 메인 파이썬 파일입니다.
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import certifi  #만약 몽고 디비 돌릴때 문제가 없으셨다면 해당 줄은 주석 처리 하세요.
client = MongoClient('mongodb+srv://test:sparta@cluster0.0mzan.mongodb.net/Cluster0?retryWrites=true&w=majority' ,tlsCAFile=certifi.where())
db = client.dbsparta
app = Flask(__name__)

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate('key/rs-object-recognition-firebase-adminsdk-r5b1b-9fae1668a5.json')
firebase_admin.initialize_app(cred)
FBdb = firestore.client()

@app.route('/')
def MainPage():
    return render_template('mainpage.html')

@app.route('/recognize_img', methods=["POST"])
def recognize():
    print(request.form)
    a = request.form(['Img_Path'])
    print(a)
    return None


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)