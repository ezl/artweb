from django.urls import include, path
from artweb.views import pics
from django.urls import include, path, re_path
from artweb.views import api

urlpatterns = [
    path('api/user/<username>', api.user_get),
    path('api/image/<uniqid>', api.image_get),
    path('pics/receive', pics.receive, name='Receive SMS'),
    path('pics/<image_id>', pics.display_image, name='Display Image')
]





