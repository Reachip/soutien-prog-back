from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenVerifySerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView
from rest_framework_simplejwt.authentication import JWTAuthentication


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

class CustomTokenVerifySerializer(TokenVerifySerializer):
    def validate(self, attrs):
        request = self.context['request']
        token = request.COOKIES.get("soutienprogtokenaccess")

        if token is None:
            token = ""

        JWTAuthentication().get_validated_token(token)
        return {}


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class TokenVerifyViewWithCookie(TokenVerifyView):
    serializer_class = CustomTokenVerifySerializer

