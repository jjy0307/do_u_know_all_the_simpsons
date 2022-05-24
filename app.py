# 페이지 구동이 되는 메인 파이썬 파일입니다.
# 플라스크와 몽고db cloud입니다
from firebase_admin import firestore
from firebase_admin import credentials
import firebase_admin
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from run_model import simpson
import requests
import certifi  # 만약 몽고 디비 돌릴때 문제가 없으셨다면 해당 줄은 주석 처리 하세요.
client = MongoClient(
    'mongodb+srv://test:sparta@cluster0.0mzan.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=certifi.where())
db = client.Simpson
app = Flask(__name__)
# firebase입니다
cred = credentials.Certificate(
    'key/rs-object-recognition-firebase-adminsdk-r5b1b-9fae1668a5.json')
firebase_admin.initialize_app(cred)
FBdb = firestore.client()

#전체 디비 넣기
# labels = ['sideshow_bob', 'mayor_quimby', 'troy_mcclure', 'lisa_simpson', 'moe_szyslak', 'groundskeeper_willie', 'sideshow_mel', 'patty_bouvier', 'waylon_smithers', 'ralph_wiggum', 'chief_wiggum', 'professor_john_frink', 'agnes_skinner', 'rainier_wolfcastle', 'otto_mann', 'miss_hoover', 'charles_montgomery_burns', 'homer_simpson', 'maggie_simpson', 'bart_simpson', 'comic_book_guy',
#               'martin_prince', 'gil', 'marge_simpson', 'lionel_hutz', 'nelson_muntz', 'snake_jailbird', 'krusty_the_clown', 'lenny_leonard', 'carl_carlson', 'abraham_grampa_simpson', 'milhouse_van_houten', 'kent_brockman', 'disco_stu', 'selma_bouvier', 'apu_nahasapeemapetilon', 'simpsons_dataset', 'fat_tony', 'cletus_spuckler', 'edna_krabappel', 'ned_flanders', 'barney_gumble', 'principal_skinner']
# for a in labels:
#     db.comments.insert_one({
#         'comments': f'hi my name is {a}',
#         'character_name': a
#     })


@app.route('/')
def MainPage():
    return render_template('mainpage.html')

@app.route('/recognize_img', methods=['POST'])
def recognize():
    img_name = request.form['Img_Path']
    result = simpson(img_name, cred)
    doc = {'img_name': img_name, 'rec_result': result}
    db.characters.insert_one(doc)
    return jsonify({'result': 'success', 'rec_result': str(result), 'rec_img': str(img_name)})


# 기존 {'fat_tony': ['1asdasdsa23213123', '123asdasdasdsadsad213123', 'aaa'], 'krusty_the_clown': ['adfadfdafdfadfaf', 'adfasdsadsadsadsadsadaf'], 'fat': ['aaaa']}
# [{'fat_tony': ['1asdasdsa23213123', '123asdasdasdsadsad213123', 'aaa']}, {'krusty_the_clown': ['adfadfdafdfadfaf', 'adfasdsadsadsadsadsadaf']}, {'fat': ['aaaa']}]

# 가현님 부분
@app.route('/wiki')
def wiki():
    dic = {}
    all_comments = list(db.comments.find({}, {'_id': False}))
    for comment in all_comments:
        if comment['character_name'] not in dic:
            dic[comment['character_name']] = [comment['comments']]
            print(dic[comment['character_name']])

        else:
            dic[comment['character_name']].append(comment['comments'])
    
    insert=[]
    for d in dic:
        insert.append({d:dic[d]})
    print(insert)
    
    #labels = ['sideshow_bob', 'mayor_quimby', 'troy_mcclure', 'lisa_simpson', 'moe_szyslak', 'groundskeeper_willie', 'sideshow_mel', 'patty_bouvier', 'waylon_smithers', 'ralph_wiggum', 'chief_wiggum', 'professor_john_frink', 'agnes_skinner', 'rainier_wolfcastle', 'otto_mann', 'miss_hoover', 'charles_montgomery_burns', 'homer_simpson', 'maggie_simpson', 'bart_simpson', 'comic_book_guy',
     #        'martin_prince', 'gil', 'marge_simpson', 'lionel_hutz', 'nelson_muntz', 'snake_jailbird', 'krusty_the_clown', 'lenny_leonard', 'carl_carlson', 'abraham_grampa_simpson', 'milhouse_van_houten', 'kent_brockman', 'disco_stu', 'selma_bouvier', 'apu_nahasapeemapetilon', 'fat_tony', 'cletus_spuckler', 'edna_krabappel', 'ned_flanders', 'barney_gumble', 'principal_skinner']
    description = {
        'sideshow_bob' : '설명', 
        'mayor_quimby' : '설명',
    }
    return render_template("wiki.html", all_comments=insert, desc=description)


# 민재님 부분
@app.route('/result')
def result():
    simpsons = list(db.characters.find({}, {'_id': False}))
    character_count = {}
    character_list = []
    character_list_count = []
    for name in simpsons:
        if name["rec_result"] in character_count:
            character_count[name["rec_result"]] += 1
        else:
            character_count[name["rec_result"]] = 1
    for cc in character_count:
        character_list.append(str(cc))
        character_list_count.append(character_count[cc])
    return render_template('result.html', labels=character_list, datas=character_list_count)


@app.route('/comment', methods=['POST'])
def comment():
    result_comment = request.form['comment']
    character_name = request.form['result']
    db.comments.insert_one({
        'comments': result_comment,
        'character_name': character_name
    })
    return jsonify({'result': 'success'})


# @app.route('/logs', methods=['GET'])
# def chart():
#     return jsonify({'result': 'success', 'categorized_results': 'character_name', '전체 심슨 캐릭터 조회 횟수': 'character_count'})

# 진영님 부분


@app.route('/modal')
def modal():
    return render_template('modal.html')


@app.route("/comments", methods=["POST"])
def comment_post():
    comment_receive = request.form['comment_give']
    character_receive = request.form['character']
    # comments_list = list(db.comments.find({}, {'_id': False}))
    # count = len(comments_list) + 1
    # doc = {
    #     'num': count,
    #     'comment': comment_receive
    # }
    doc = {
        'comments': comment_receive,
        'character_name': character_receive
    }
    db.comments.insert_one(doc)

    return jsonify({'msg': '작성 완료!'})


# @app.route("/comments", methods=["GET"])
# def comment_get():
#     comments_list = list(db.comments.find({}, {'_id': False}))
#     return jsonify({'comments': comments_list})


@app.route("/delete", methods=["POST"])
def comment_del():
    # num = request.form['count']
    # db.comments.delete_one({'num': int(num)})
    com = request.form['comment']
    name = request.form['character_name']
    db.comments.delete_one({'comments':com, 'character_name':name})
    return jsonify({'msg': '삭제 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
