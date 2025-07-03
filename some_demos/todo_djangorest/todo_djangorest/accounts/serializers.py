from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) # wont be returned in the response as its write only
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user


class LoginRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    #returns accessToken, refresh TOken

class LoginResponseSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()
    message = serializers.CharField()

class LogoutRequestSerializer(serializers.Serializer):
    refresh = serializers.CharField()

class LogoutResponseSerializer(serializers.Serializer):
    message = serializers.CharField()