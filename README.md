# What is it
```
neis api를 통해서 학사일정을 받아와 DB에 저장하는 api입니다.
해당 api는 일주일, 한달, 일년로 나누어서 크롤링할 수 있습니다.
```
# How to Use

## 0. .env 파일 생성
1. 가장 최상위 파이엘 .env 파일 생성 <br>
2. 해당 파일에 노션에 [인수인계 -> 백엔드 -> 스케쥴](https://www.notion.so/xquare-app/env-8c6f95c4c1e5498388ee5cbd80dbbc7d?pvs=4)에 들어가면 있는 .env 값을 복사해 넣는다

## 1.라이브러리 설치

```
pip install -r requirements.txt
```

## 2.서버 실행

```
python3 -m src.main
```

## 3.테스트
```
0.0.0.0:8000/docs
```
fastapi에서는 프레임워크에서 스웨거를 지원하기 때문에 해당 주소를 웹페이지에 입력하면 스웨거로 테스트할 수 있다.<br>
<br>
<br>
<br>
<br>
**문제 발생시 슬랙에서 @김승진 찾아주세요**
