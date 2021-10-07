from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import InstaUser, InstaBlogger

class InstaBloggerSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstaBlogger
        fields = ['id', 'blogger_name']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class InstaUserSerializer(serializers.ModelSerializer):
    user_follower = InstaBloggerSerializer(read_only=True)
    class Meta:
        model = InstaUser
        fields = ['id', 'user_id', 'user_follower']

class InstaUserFullSerializer(serializers.ModelSerializer):
    user_follower = InstaBloggerSerializer(read_only=True)
    class Meta:
        model = InstaUser
        fields = ['id', 'user_id', 'user_follower', 'user_login']
