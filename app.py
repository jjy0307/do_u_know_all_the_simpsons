# 페이지 구동이 되는 메인 파이썬 파일입니다.
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsimpson


@app.route('/')
def home():
    return render_template('modal.html')


@app.route('/modal/comment', methods=["GET"])
def comment_get():
    comment = request.args.get('id')
    comments = list(db.comments.find({'comment': comment}, {'_id': False}))

    msg = 'comment_listing is called'
    return jsonify({'comments': comments, 'msg': msg})


@app.route("/modal/comment", methods=["POST"])
def comment_post():
    comment_receive = request.form['comment_give']
    comment_info = {
        'comment': comment_receive,
    }
    db.comments.insert_one(comment_info)

    msg = 'comment_save is called'
    return jsonify({'msg': msg})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
