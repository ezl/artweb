from core.models import User
from sms.models.image import Image
from rest_framework import serializers


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'id',
            'url',
            'views',
            'mime_type',
            'created_at',
            'user_username',
            'user_phone',
            'user_email',
            'user_full_name',
            'user_location',
            'user_profile_url',
            'user_created_at'
        ]


class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'id',
            'url',
            'views',
            'mime_type',
            'created_at'
        ]


class UserSerializer(serializers.ModelSerializer):
    images = UserImageSerializer(many=True)

    class Meta:
        model = User
        fields = [
            'username',
            'phone',
            'email',
            'full_name',
            'location',
            'country',
            'state',
            'city',
            'zip',
            'profile_url',
            'created_at',
            'images'
        ]
