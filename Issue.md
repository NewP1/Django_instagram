# Django migation error 
```bash
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
```
__제일 처음 'runserver'명령을 수행했을 때 발생__

- __You have 18 unapplied migration(s).__ 부분은 18개의 적용이 안된 'migration'이 있다'
- 이와 관련 앱들이 'admin', 'auth', 'contenttypes', 'sessions'라고 되어있는데, 이 앱들은 장고 프로젝트를 만들었을 때에 자동으로 만들어지는 앱들이다.
- 관련된 정보는 'config'폴더의 'settings.py'파일에서 확인할 수 있다.
```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```
'message', 'staticfiles'는 데이터베이스와는 상관없는 앱들

('migation'이 필요한 경우는 데이터베이스가 필요한 경우이다.)

> 'settings.py'파일에는 설치된 앱들과 사용하는 데이터베이스의 정보 확인
---

### 해결
```bash
python manage.py makemigrations
python manage.py migrate
```
- `makemigrations`을 실행하면 모델을 변경시킨 사실 또는 새로 생성한 모델드롸 같은 변경사항을 migrations로 저장하고자 Django에 알려줌 
    - 즉, 변경사항 저장
- `migrate`는 적용되지 않은 생성/변경된 migrations들의 파일을 데이터베이스에 적용
---