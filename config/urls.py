from django.urls import path
from sms.views import pics, api
from django.contrib import admin

urlpatterns = [
    path('api/status', api.api_status),
    path('api/user/<username>', api.user_get),
    path('api/image/<uniqid>', api.image_get),
    path('pics/receive', pics.receive, name='Receive SMS'),
    path('pics/<image_id>', pics.display_image, name='Display Image'),
    path('admin/', admin.site.urls),
]
