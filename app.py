#페이지 구동이 되는 메인 파이썬 파일입니다.
#플라스크와 몽고db cloud입니다
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from run_model import simpson
import certifi  #만약 몽고 디비 돌릴때 문제가 없으셨다면 해당 줄은 주석 처리 하세요.
client = MongoClient('mongodb+srv://test:sparta@cluster0.0mzan.mongodb.net/Cluster0?retryWrites=true&w=majority' ,tlsCAFile=certifi.where())
db = client.Simpson
app = Flask(__name__)
#firebase입니다
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
    img_name = request.form['Img_Path']
    result = simpson(img_name, cred)
    doc = {'img_name': img_name, 'rec_result': result}
    db.characters.insert_one(doc)
    return jsonify({'result': 'success', 'rec_result': result})








if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
