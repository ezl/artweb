from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from artweb.users.models import User
from artweb.models.image import Image
from artweb.serializers import UserSerializer, ImageSerializer

@api_view(['GET'])
def user_get(request, username: str):
    """
    Retrieve specific user profile, including all images assigned to them.
    """

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    ser = UserSerializer(user)
    return Response(ser.data)

@api_view(['GET'])
def image_get(request, uniqid: str):
    """
    Retrieve details of specific image.
    """
    try:
        img = Image.objects.get(uniqid=uniqid)
    except Image.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    ser = ImageSerializer(img)
    return Response(ser.data)


