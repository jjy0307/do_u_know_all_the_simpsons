from pymongo import MongoClient
from collections import Counter
import jwt
from flask import Flask, render_template, request, jsonify
from werkzeug.debug import console

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

client = MongoClient('localhost', 27017)
db = client.characters
SECRET_KEY = 'simpsons'


@app.route('/')
def home():
    return render_template('result.html')


@app.route('/comment', methods=['POST'])
def comment():
    result_comment = request.form['comment']
    db.comment.insert_one({
        'comments': result_comment
    })
    return jsonify({'result': 'success'})


@app.route('/')
def chart():
    token_receive = request.cookies.get('mytoken')
    payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
    user_info = db.users.find_one({"categorized_results": payload['categorized_results']})

    return render_template('result.html', categorized_results=user_info["categorized_results"])


@app.route('/logs', methods=['GET'])
def chart():
    simpsons = list(db.characters.find({}, {'_id': False}))
    character_count = []
    for name in simpsons:
        if name["character_name"] in character_count:
            character_count[name["character_name"]] += 1
        else:
            character_count[name["character_name"]] = 1
    return jsonify({'result': 'success', 'categorized_results': 'character_name', '전체 심슨 캐릭터 조회 횟수': 'character_count'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
