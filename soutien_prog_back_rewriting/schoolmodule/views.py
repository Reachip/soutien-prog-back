from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import SchoolModule
from .serializers import SchoolModuleSerializer


class SchoolModuleViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolModuleSerializer
    queryset = SchoolModule.objects.all()

    def get_permissions(self):
        permission_classes = []

        if self.action == "create":
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]
