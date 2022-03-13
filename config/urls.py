from django.urls import include, path
from django.urls import include, path, re_path
from sms.views import pics, api

urlpatterns = [
    path('api/user/<username>', api.user_get),
    path('api/image/<uniqid>', api.image_get),
    path('pics/receive', pics.receive, name='Receive SMS'),
    path('pics/<image_id>', pics.display_image, name='Display Image')
]





