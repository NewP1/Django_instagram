"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import Main

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', Main.as_view())
]

'''
urlpatterns는 우리의 서버 주소 뒤에 특정 주소를 더해서 어떤 프로그램을 실행시킬지 결정해주는 역할

위를 예시로
http://127.0.0.1:8000/admin/ 으로 접속하면 admin.site.urls를 실행한다는 의미이다.

우리가 만든 페이지는 html파일로 만들 수 있다
'''