from rest_framework import viewsets
from soutien_prog_back_rewriting.permissions import IsAuthenticatedWithJWTInCookie
from .models import SchoolModule
from .serializers import SchoolModuleSerializer


class SchoolModuleViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolModuleSerializer
    queryset = SchoolModule.objects.all()

    def get_permissions(self):
        permission_classes = []

        if self.action == "create":
            permission_classes = [IsAuthenticatedWithJWTInCookie]

        return [permission() for permission in permission_classes]
