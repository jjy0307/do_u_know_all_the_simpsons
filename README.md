# 🍩 Do u know all the Simpson's?

## 📄 프로젝트 소개
심슨 사진 입력시 머신러닝 모델이 학습한 데이터를 바탕으로 캐릭터 이름을 출력해주는 서비스 + 사용자가 해당 캐릭터에 관련한 내용을 자유롭게 추가하고 삭제할 수 있는 서비스

### ⏲ 개발 기간 : 2022.5.19 ~ 2022.5.24

### 소개 영상  [youtube](https://youtu.be/fsRijEg7DeM)

### Github  [Code](https://github.com/Reinforcement-succeeded/do_u_know_all_the_simpsons)

## 🧑 팀 구성 
* 4인 팀 프로젝트  <br>
* 맡은 역할 : AI engineer / back-end developer / front-end developer

<table>
  <tr>
    <td align="center"><strong>구분</strong></td>
    <td align="center"><strong>Back-end</strong></td>
    <td align="center"><strong>Front-end</strong></td>
    <td align="center"><strong>Designer</strong></td>
    <td align="center"><strong>AI Engineer</strong></td>	  
  </tr>
  <tr>
    <td align="center"><strong>메인페이지</strong></td>
    <td align="center">이승태</td>
    <td align="center">이승태</td>
    <td align="center">이승태</td>
    <td rowspan="4" align="center">윤가현</br>전진영</td>
  </tr>
  <tr>
    <td align="center"><strong>결과 페이지</strong></td>
    <td align="center">김민재</td>
    <td align="center">김민재</td>
    <td align="center">김민재</td>
  </tr>
  <tr>
    <td align="center"><strong>모달 페이지</strong></td>
    <td align="center">전진영</td>
    <td align="center">전진영</td>
    <td align="center">전진영</td>
  </tr>
  <tr>
    <td align="center"><strong>위키 페이지</strong></td>
    <td align="center">윤가현</td>
    <td align="center">윤가현</td>
    <td align="center">윤가현</td>
  </tr>
</table>

## ✨ Stack
* Language : Python, Javascript
* Framework : Flask
* Database : MongoDB Cloud
* Infra : Firebase

## 📖 Stack & Library Version

## 🕹 주요 기능
- **메인페이지에서 사용자가 이미지 업로드 -> 머신러닝 모델이 이를 인식하여 해당 이미지의 카테고리를 결과페이지에 출력**

- **인식한 심슨이미지와 라벨 데이터를 DB에 저장**

**추가기능 (완료한 것은 굵게 표시)**
- 데이터 추가 학습
- <u>**많이 조회된 캐릭터를 GET으로 가져와 결과페이지에 그래프로 출력**</u>
  - (어떤 심슨 캐릭터가 가장 많이 조회되었는지, 알려지지 않은 캐릭터가 많이 조회되었을 것이라 예상됨)
- 이미지 결과 공유 기능 (og태그 이용 : 시간 남을 경우 진행)
- <u>**검색기능을 가진 심슨 위키 페이지 제작**
- **심슨 위키페이지에서 DB내용(캐릭터이름, 사진, 코멘트)과 서버에서 작성된 설명 가져와 jinja2로 페이지 띄우기**
- **파이어베이스 이용해 메인페이지에서 이미지 드래그-드롭기능 구현**
- **심슨 위키페이지에서 모달 띄운 뒤 DB연동해 코멘트 추가, 삭제할 수 있는 기능 제작**</u>

**사용한 모델** 

[custom된 CNN](https://colab.research.google.com/drive/1pmOUV6U1nJE5f10yM2-iDDFp-1W2p1ut?usp=sharing)

**데이터셋**

**[The Simpsons Characters Data](https://www.kaggle.com/datasets/alexattia/the-simpsons-characters-dataset)**



### **개발 일정**
![](https://velog.velcdn.com/images/soyoyun/post/4bc2a1c6-fe19-4f30-a496-898d07b8207a/image.png)


### 최종 **레이아웃**
![](https://velog.velcdn.com/images/soyoyun/post/2bc7df3c-c941-4d13-b574-381a28dab5b8/image.png)


### **API 설계**
![](https://velog.velcdn.com/images/soyoyun/post/f4c5feaa-accd-4400-a9e7-a7a258b319c1/image.png)


---
### 제작 완료**
   
   
### 사용된 머신러닝 모델
**[custom된 CNN 모델 이용](https://colab.research.google.com/drive/1pmOUV6U1nJE5f10yM2-iDDFp-1W2p1ut?usp=sharing)**


### 머신러닝 모델 실험 결과
 - 각각 다른 모델 3개로 실험 해본 결과 상이한 결과를 보이거나 유의미한 차이가 나지 않았음.
- tensorflow로 설계된 CNN 모델 2개, pytorch로 설계된 Resnet18 모델 1개


**모델 실험 결과**<br>
**1) [custom_1 CNN (92%)](https://colab.research.google.com/drive/1pmOUV6U1nJE5f10yM2-iDDFp-1W2p1ut?usp=sharing) : 이번 프로젝트에서 사용됨**
        
```python
        Epoch 1/50
        189/189 [==============================] - 105s 484ms/step - loss: 3.1456 - accuracy: 0.1013 - val_loss: 2.9746 - val_accuracy: 0.1671
       ...
        Epoch 50/50
        189/189 [==============================] - 90s 477ms/step - loss: 0.3779 - accuracy: 0.8928 - val_loss: 0.4056 - val_accuracy: 0.9229
```
 
2) [custom_2 CNN (95%)](https://colab.research.google.com/drive/1ecvw5GMOvepKF6Q7t6EwyyHAtH9rCWRf?usp=sharing)

<img src="https://velog.velcdn.com/images/soyoyun/post/4831eaf1-a18f-461e-84b5-4861de984911/image.png" width=400px height=300px>

3) [Resnet18 (95%)](https://colab.research.google.com/drive/1nYEqyZcVjpsv4CmrCsE20rl4x_Oh4CHK?usp=sharing)

<img src="https://velog.velcdn.com/images/soyoyun/post/8317e84e-4322-4506-9b6f-4decfef356c2/image.png" width=400px height=500px>

    
**드라이브에서 머신러닝 파일 공유하며 프로젝트 진행**
![](https://velog.velcdn.com/images/soyoyun/post/8d0e8160-18b6-44e1-8ab8-0a66dae351e0/image.png)


### 메인페이지-결과페이지
   ![](https://velog.velcdn.com/images/soyoyun/post/e238a6dd-3753-4d17-a808-283063805ee0/image.gif)

 **이미지 드래그앤 드롭**
- 사진을 `Firebase`에 저장한 뒤 URL을 DB에 저장하는 방식으로 진행하였고, cookie에 사진 URL과 모델이 예측한 결과값을 저장해 이를 결과페이지에서 활용하였다.
 - 이미지 드래그 후 ‘Find simpson’ 버튼을 누르면 결과페이지로 이동한다.
     
 - 자바스크립트를 이용하여 차트로 어떤 캐릭터가 많이 조회되었는지 보여주었다.
        - chart에 데이터를 jinja2로 보낼때 `'` 라는 특수문자가 HTML상에서`&#38`라고 읽히면서 전체 문자열이 `&#38string&#38`로 읽히는 현상이 발생했는데 이를 `|safe`로 해결하였다.
        
![](https://velog.velcdn.com/images/soyoyun/post/77132d91-1fb9-4893-aa64-ce314c7c6051/image.gif)

- ‘나무위키’처럼 사용자가 결과 화면에 띄워진 캐릭터에 관한 설명을 쓸 수 있게 구현하였다. ‘Post!’버튼을 누를 시 모델이 예측한 캐릭터이름(character_name)과 작성한 설명(comments)이 DB의 ‘Simpson/comments’에 저장된다.
**(위키페이지내 모달창에서 입력한 설명을 삭제 및 추가가 가능하다)**
    
---

### 위키페이지-모달페이지 
![](https://velog.velcdn.com/images/soyoyun/post/284378fd-3583-4659-8f77-0a61c0197600/image.gif)

 - 자바스크립트로 심슨 캐릭터를 검색하면 찾아질수 있게 구현하였다.
- 심슨 캐릭터 클릭시 모달을 띄워 해당 심슨 캐릭터의 이름, 이미지, 캐릭터 설명, 댓글이 나오게 DB를 연동시켰다.
    
- jinja2를 사용하여 `wiki.html`페이지를 구현하였다.
        - Simpson/comments DB안에 있는 데이터(comments, character_name)를 모두 가져와 원하는 심슨 캐릭터 에 댓글을 달 수 있도록`app.py`를 구성하였다.
        - 심슨 캐릭터를 클릭할 시 해당 심슨의 모달을 띄워 Simpson/comments DB에서 캐릭터의 이름과 달린 설명을 가져오고 app.py에서 작성된 캐릭터 설명도 가져온 뒤 이를 모달창에서 모두 보여질 수 있도록 구현하였다. 보이는 것처럼 jinja2의 반복문, 조건문을 이용해 한 줄에 5명의 심슨 캐릭터가 띄워지도록 `wiki.html`를 제작하였다.

---
### 전체 동작 과정

**메인페이지(사진 입력) → 결과페이지(사진, 캐릭터 라벨 출력 후 캐릭터 설명 입력) → 위키 페이지(캐릭터 검색 후 달린 설명 확인 및 삭제,추가 가능 확인)**
![](https://velog.velcdn.com/images/soyoyun/post/851ca185-ecbf-413d-bf8d-3cf626ac8e5c/image.gif)

![](https://velog.velcdn.com/images/soyoyun/post/c3c9264c-c3af-46be-aa2d-c45315b1f049/image.gif)


## **발표 후 피드백**

- 모달에 댓글 달고 삭제시 새로고침되는 부분 다른 방법 구상하기
- PR리뷰 데일리별로 머지하는 방식으로 진행하기 
- 코드분리 굿 ( app.py 함수별로 빼놓은것 👍 ) 
- description → json형태로 빼놓고 불러오는 방식 사용하는 것을 추천

```python
# description.py

def des():
	description = {}
	return description
```

```python
# app.py

from descripition import des

#description 들어갈 곳에
description = des()
```

**[ 매일 기록 _ 진영 ]**

- 0518/각각 이미지마다 모달창
- 0519/코멘트 작성 구현중
- 0520/코멘트 작성, 삭제 구현 완료 / 캐릭터 기본 정보 입력
-   (1번을 그래프로 표현하기 : 어떤 캐릭터가 가장 많이조회되었는지, 알려지지않은캐릭터가 많을것이라 예상됨)

---

**[ 매일 기록 _ 가현 ]**

-   0518/Notion 팀 페이지 개설 후 회의 내용 기록 및 정리, 모델 2개 학습 후 정확도(val_acc) 비교 (CNN-전이학습:약 50%, CNN-custom:약 92%)
-   0519/모델 1개 학습 (CNN-custom-2), 위키페이지 DB연동 관련 자료 서치 
-   0520/팀원 오류 디버깅(CNN부분 이미지 불러오기 부분, 차트-DB 연동부분 DB이해 도움), jinja2 이용해 심슨API 웹에 띄우기, ajax , fetch, axios, jinja 서칭
 - 이때 API 사용하여 위키페이지 구현해보고 싶었는데 페이지 로딩이 느려서 샘플 가져오는 용으로만 사용하기로함
-   0522/위키페이지 js함수 이용해 검색기능 구현, 페이지 flex이용해 구현 후 페이지 이동기능 js함수로 토글기능 넣어서 구현
 - 고민해본 점 : 위키페이지에 샘플 미리 넣어놓고 작업 or 데이터 불러와 작업
-   0523/위키페이지 디버깅, 깃허브 토큰-sourcetree 설정 오류 해결, DB-위키페이지 jinja2 이용하여 연동
-   0524/위키페이지 디버깅, 최종파일에서 css 작업(마무리), 발표할 자료 정리 및 Readme 업데이트

---

**[ 매일 기록 _ 승태 ]**

- 0518/Github 레포지터리 생성, ReadMe 작성, API설계, 메인페이지 생성, 이미지 업로드 구현
- 0519/Firebase 연결 구현, axios 연결, drag&drop 활용, 가상환경 설정
- 0520/심슨 예측 모델 구현
- 0523/전체페이지 병합, 쿠키 메인페이지에서 결과페이지로 결과 전송
- 0524/jinja2로 위키페이지, 결과페이지에 결과전송

---

**[ 매일 기록 _ 민재 ]**

- 0518/팀 회의에서 페이지 설꼐 후 이후 결과 페이지 HTML 작성, 페이지에 필요한 기능들 검색
- 0519/결과 페이지 입력창에 평가 작성시 입력창에 있는 내용이 DB에 저장되도록 구현
- 0520/결과 이미지의 결과를 받아서 그래프에 표에 나타내기 구현에 생긴 오류 고치기
- 0523/결과 이미지의 결과를 받아서 그래프에 표에 나타내기 구현
- 0524/결과 페이지 모르는 부분 이해하기 코드 정리
