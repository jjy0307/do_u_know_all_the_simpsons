from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

client = MongoClient('localhost', 27017)
db = client.result


@app.route('/')
def home():
    return render_template('result.html')


@app.route('/comment', methods=['POST'])
def comment():
    result_comment = request.form['comment']
    db.comment.insert_one({
        'comment': result_comment
    })
    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5002, debug=True)
