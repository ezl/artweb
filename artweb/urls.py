from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('pics/', include('sms2url.urls')),
    path('admin/', admin.site.urls),
]

