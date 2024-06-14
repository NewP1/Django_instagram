from django.urls import path
from .views import Login, Join, LogOut, UpdateProfile

'''
urlpatterns는 우리의 서버 주소 뒤에 특정 주소를 더해서 어떤 프로그램을 실행시킬지 결정해주는 역할

위를 예시로
http://127.0.0.1:8000/admin/ 으로 접속하면 admin.site.urls를 실행한다는 의미이다.

우리가 만든 페이지는 html파일로 만들 수 있다
'''

urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('join', Join.as_view(), name='join')
]


