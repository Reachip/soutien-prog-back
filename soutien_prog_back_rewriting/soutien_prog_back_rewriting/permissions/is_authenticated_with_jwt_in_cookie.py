from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import BasePermission

class IsAuthenticatedWithJWTInCookie(BasePermission):
    def has_permission(self, request, view):
        try:
            JWTAuthentication().jwt_a.get_validated_token(request.COOKIES["soutienprogtokenaccess"])
            return True

        except Exception:
            return False
