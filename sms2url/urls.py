from django.urls import path
from . import views

urlpatterns = [
    path('receive', views.receive, name='Receive SMS'),
    path('<image_id>', views.display_image, name='Display Image')
]



