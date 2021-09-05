from jwt import decode
import os
from rest_framework.permissions import BasePermission

class IsAuthenticatedWithJWTInCookie(BasePermission):
    def has_permission(self, request, view):
        try:
            decode(request.COOKIES["soutienprogtokenaccess"], os.environ['DJANGO_SECRET_KEY'], 'HS256')
            return True

        except Exception:
            return False
