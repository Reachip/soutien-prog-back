import datetime
import os
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.serializers import Serializer
from rest_framework.views import APIView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication

from jwt import decode
from rest_framework import serializers
from rest_framework.response import Response

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')

class UserView(APIView):
    def get(self, request, *args, **kwargs):
        jwt = decode(request.COOKIES["soutienprogtokenaccess"], os.environ['DJANGO_SECRET_KEY'], 'HS256')
        instance = get_object_or_404(get_user_model(), username=jwt["username"])
        return Response(UserSerializer(instance).data)

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username

        return token

class CustomTokenVerifySerializer(Serializer):
    def validate(self, attrs):
        request = self.context["request"]
        token = request.COOKIES.get("soutienprogtokenaccess")

        if token is None:
            token = ""

        JWTAuthentication().get_validated_token(token)
        return {}


class LogoutWithCookie(APIView):
    def post(self, request):
        response = Response({})
        response.set_cookie(
            "soutienprogtokenaccess", "", expires=datetime.datetime(1970, 1, 1)
        )
        
        response.set_cookie(
            "soutienprogtokenrefresh", "", expires=datetime.datetime(1970, 1, 1)
        )

        return response


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class TokenVerifyViewWithCookie(TokenVerifyView):
    serializer_class = CustomTokenVerifySerializer
