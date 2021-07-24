from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import BasePermission

class IsAuthenticatedWithJWTInCookie(BasePermission):
    def has_permission(self, request, view):
        jwt_a = JWTAuthentication()

        try:
            jwt_a.get_validated_token(request.COOKIES["soutienprogtokenaccess"])
            return True

        except Exception:
            return False
