import pdb

import jwt
from django.utils.deprecation import MiddlewareMixin
from rest_framework.utils import json


class SetJWTOnCookieHttpOnly(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        if response.content:
            if request.path == '/api/auth/':
                tokens = json.loads(response.content)
                response.set_cookie("soutienprogtokenaccess", tokens["access"])
                response.set_cookie("soutienprogtokenrefresh", tokens["refresh"])

            elif request.path == '/api/refresh/':
                tokens = json.loads(response.content)
                response.set_cookie("soutienprogtokenaccess", tokens["access"])

        return response
