from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import CourseSerializer
from .models import Course


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_permissions(self):
        permission_classes = []

        if self.action == "create":
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]
