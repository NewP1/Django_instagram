from django.shortcuts import render
from rest_framework.views import APIView
from content.models import Feed

from rest_framework.response import Response
import os
from .settings import MEDIA_ROOT
from uuid import uuid4

class Main(APIView):
    def get(self, request):
        '''
        만든 모델 활용하는 코드

        object 붗여서 모델 안 데이터를 다룰 수 있다.

        => feed_list에 Feed라는 모델 안에 있는 모든 데이터를 넣는 코드

        데이터가 여러개라면 List 형태로 만들어짐
        feed_list = [Feed1, Feed2, Feed3, ...]
        '''        
        feed_list = Feed.objects.all()

        # key = feed_list, value = feed_list
        return render(request, 'insta/main.html', context=dict(feed_list=feed_list))
    
class UploadFeed(APIView):
    def post(self, request):
        file = request.FILES['file']
        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        content = request.data.get('content')
        image = uuid_name
        profile_image = request.data.get('profile_image')
        user_id = request.data.get('user_id')

        Feed.objects.create(content=content, image=image, profile_image=profile_image, user_id=user_id, like_count=0)

        return Response(status=200)