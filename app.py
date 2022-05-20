# 페이지 구동이 되는 메인 파이썬 파일입니다.
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsimpson


@app.route('/')
def home():
    return render_template('modal.html')


@app.route("/comments", methods=["POST"])
def comment_post():
    comment_receive = request.form['comment_give']
    comments_list = list(db.comments.find({}, {'_id': False}))
    count = len(comments_list) + 1

    doc = {
        'num': count,
        'comment': comment_receive
    }

    db.comments.insert_one(doc)

    return jsonify({'msg': '작성 완료!'})


@app.route("/comments", methods=["GET"])
def comment_get():
    comments_list = list(db.comments.find({}, {'_id': False}))
    return jsonify({'comments': comments_list})

@app.route("/delete", methods=["POST"])
def comment_del():
    num = request.form['count']
    db.comments.delete_one({'num': int(num)})

    return jsonify({'msg': '삭제 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
