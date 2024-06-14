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
from django.urls import path, include
from .views import Main
from django.conf import settings
from django.conf.urls.static import static

'''
urlpatterns는 우리의 서버 주소 뒤에 특정 주소를 더해서 어떤 프로그램을 실행시킬지 결정해주는 역할

위를 예시로
http://127.0.0.1:8000/admin/ 으로 접속하면 admin.site.urls를 실행한다는 의미이다.

우리가 만든 페이지는 html파일로 만들 수 있다
'''

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', Main.as_view()),
    path('content/', include('content.urls')),
    path('user/', include('user.urls'))
]


'''
static은 서버를 돌릴 때 필요한 파일들, media는 사용자가 올리는 파일들을 관리하는 곳

'content/upload'로 접속할 경우 UploadFeed를 실행

아래 코드가 media 경로를 url에 포함하는 코드이다.
이걸 해줘야 파일을 올리면 ~/media/{파일이름}으로 조회할 수 있다.
'''

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


