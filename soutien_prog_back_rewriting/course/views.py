from rest_framework import viewsets
from soutien_prog_back_rewriting.permissions import IsAuthenticatedWithJWTInCookie


from .serializers import CourseSerializer
from .models import Course


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_permissions(self):
        permission_classes = []

        if self.action == "create":
            permission_classes = [IsAuthenticatedWithJWTInCookie]

        return [permission() for permission in permission_classes]
