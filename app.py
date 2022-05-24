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
            # print(dic[comment['character_name']])

        else:
            dic[comment['character_name']].append(comment['comments'])
    
    insert=[]
    for d in dic:
        insert.append({d:dic[d]})
    print(insert)
    
    #labels = ['sideshow_bob', 'mayor_quimby', 'troy_mcclure', 'lisa_simpson', 'moe_szyslak', 'groundskeeper_willie', 'sideshow_mel', 'patty_bouvier', 'waylon_smithers', 'ralph_wiggum', 'chief_wiggum', 'professor_john_frink', 'agnes_skinner', 'rainier_wolfcastle', 'otto_mann', 'miss_hoover', 'charles_montgomery_burns', 'homer_simpson', 'maggie_simpson', 'bart_simpson', 'comic_book_guy',
     #        'martin_prince', 'gil', 'marge_simpson', 'lionel_hutz', 'nelson_muntz', 'snake_jailbird', 'krusty_the_clown', 'lenny_leonard', 'carl_carlson', 'abraham_grampa_simpson', 'milhouse_van_houten', 'kent_brockman', 'disco_stu', 'selma_bouvier', 'apu_nahasapeemapetilon', 'fat_tony', 'cletus_spuckler', 'edna_krabappel', 'ned_flanders', 'barney_gumble', 'principal_skinner']
    description = {"sideshow_bob":"I don't agree with his Bart-killing policy, but I do approve of his Selma-killing policy.",
                    "mayor_quimby":"Can't we have one meeting that doesn't end with us digging up a corpse?", 
                    "troy_mcclure":"Ahh! Sweet liquor eases the pain.",
                    "lisa_simpson":"These are my only friends...grown-up nerds like Gore Vidal. And even he's kissed more boys than I ever will.",
                    "moe_szyslak":"When I catch you, I'm gonna pull out your eyes and stick 'em down your pants so you can watch me kick the crap outta you, okay? Next I'm gonna use your tongue to paint my boat!",
                    "groundskeeper_willie":" Back in Edinburg, we had a coal miners strike. All we wanted were hats with a wee light on top. Then one day the mine collapsed. No one made it out alive, not even Willie!",
                    "sideshow_mel":"They say any publicity is good publicity.",
                    "patty_bouvier":"Some days at the DMV, we don't let the line move at all. We call those weekdays.",
                    "waylon_smithers":"I think women and seamen don't mix",
                    "ralph_wiggum":"They taste like...burning.",
                    "chief_wiggum":"When I look at people I don't see colors; I just see crackpot religions.",
                    "professor_john_frink":"Professor Frink is voiced by Hank Azaria. The character was originally written as a mad scientist.",
                    "agnes_skinner":"Agnes Skinner is the strict and bitter mother of Seymour Skinner. She's very harshly controlling of her son and treats him like a mother would do to a small child, once grounding him because he did not say who was at the door after answering it. ",
                    "rainier_wolfcastle":"My eyes! The goggles do nothing!",
                    "otto_mann":"Oh, wow, windows. I don't think I could afford this place.",
                    "miss_hoover":"Elizabeth Hoover, B.Ed. (also known as Miss Hoover) is a recurring character on The Simpsons. She is a second grade teacher at Springfield Elementary School.",
                    "charles_montgomery_burns":"Doughnuts? I told you I don't like ethnic food",
                    "homer_simpson":"I hope I didn't brain my damage.",
                    "maggie_simpson":"It's your fault I can't talk!",
                    "bart_simpson":"Eat my shorts",
                    "comic_book_guy":"Last night's 'Itchy & Scratchy' was, without a doubt, the worst episode ever. Rest assured that I was on the Internet within minutes, registering my disgust throughout the world.",
                    "martin_prince":"Pick me, teacher, I'm ever so smart!",
                    "gil":"Gilbert Gunderson (usually referred to as Ol' Gil or just simply Gil) is an unsuccessful and unlucky businessman of Springfield.",
                    "marge_simpson":"I'm sleeping in the bath tub.",
                    "lionel_hutz":"HEY, YOU! GET OUT OF MY OFFICE!",
                    "nelson_muntz":"Shoplifting is a victimless crime, like punching someone in the dark.",
                    "snake_jailbird":"...Bye! / See ya, cops! / Hoa! / Dude!",
                    "krusty_the_clown":"Hoohoohoohahaha!",
                    "lenny_leonard":"Lenford 'Lenny' Leonard (born April 13, 1955) is a recurring character in The Simpsons, and a supporting character in The Simpsons Movie. ",
                    "carl_carlson":"See, statements like that are why people think we're gay.",
                    "abraham_grampa_simpson":"Why are you pleople avoiding me? Does my withered face remind you of the grim specter of death?",
                    "milhouse_van_houten":"Remember the time he ate my goldfish? And you lied and said I never had a goldfish. Then why did I have the bowl, Bart? Why did I have the bowl?",
                    "kent_brockman":"I've said it before and i'll say it again, democracy simply doesn't work",
                    "disco_stu":"Disco Stu wishes he'd gone as Marilyn McCoo.",
                    "selma_bouvier":"How's my blubber in-law?",
                    "apu_nahasapeemapetilon":"By chilling my loins I increase the chances of impregnating my wife.",
                    "fat_tony":"I don't get mad, I get stabby.",
                    "cletus_spuckler":"Cletus Delroy Montfort Bigglesworth Spuckler, also known as Cletus the Slack-Jawed Yokel, is a stereotypical redneck with a good-natured personality.",
                    "edna_krabappel":"These tests will have no effect on your grades. They merely determine your future social status and financial success. If any.",
                    "ned_flanders":"Howdily-doodily, neighborino!",
                    "barney_gumble":"BURRRRRRPPPP!",
                    "principal_skinner":"Hello, Simpson. I'm riding the bus today becuase Mother hid my car keys to punish me for talking to a woman on the phone. She was right to do it."}
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
    print('aa')
    print(comment_receive)
    print(character_receive)
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
