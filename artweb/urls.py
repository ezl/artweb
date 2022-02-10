from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('sms2url/', include('sms2url.urls')),
    path('admin/', admin.site.urls),
]

