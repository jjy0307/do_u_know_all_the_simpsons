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
# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': "1:95927745266:web:9ce88f8d96b5c338846e6b",
})

FBdb = firestore.client()

@app.route('/')
def MainPage():
    return render_template('mainpage.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)