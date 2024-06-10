# MTV(Model, Template, View)

- 웹 서비스는 model, template, view 3가지로 분리

## Model

- model은 데이터의 형태를 의미

    ```
    ex)
    피드 - {본문, 사진, 프로필사진, 아이디, 좋아요 수}
    추천인 - {프로필사진, 아이디, 추천 이유}

    등
    ``` 

```
1단계
모델 이름과 데이터 나열

모델명 - 피드
본문
사진
프로필사진
아이디
좋아요 수
```
```python
# 2단계 
# 영어로 써보기

class Feed
    content
    image
    profile_image
    user_id
    like_count
```
```python
# 3 + a단계
# 코드 작성

class Feed(models.Model):
    content         = models.TextField()
    image           = models.TextField()
    profile_image   = models.TextField()
    user_id         = models.TextField()
    like_count      = models.IntegerField()
```
---
이제 다양한 model들을 생성해 웹 서비스를 관리해야 한다.

그럼 어디다가 소스를 저장하면 좋을까


__장고는 APP단위로 소스를 관리할 수 있다.__

APP을 만드는 것은 명령어 한줄로 가능

```bash
python manage.py startapp (앱이름)

# ex) python manage.py startapp content
```

이후 models.py 에 모델들 추가.

__model을 만들었으면 데이터베이스(DB)를 만드는 작업이 필요__


## DB

모델을 만들고 DB 생성해줘야 함

- config/setting.py에 INSTALLED_APPS에 앱이름(현 프로젝트에서는 content)를 추가해줘야 함
    - Django에게 우리가 명령어로 만든 앱을 사용하겠다고 명시하는 과정

```bash
python manage.py makemigrations
python manage.py migrate
```

- `makemigrations`는 우리가 만든 models.py를 DB에 반영하기 위한 <b>스크립트</b>를 작성하는 명령어
- `migrate`는 그 <b>스크립트</b>를 실행하는 명령어


> 테이블 확인은 db.sqlite3<br><br>
> (Django는 기본적으로 sqlite3를 DB로 사용)