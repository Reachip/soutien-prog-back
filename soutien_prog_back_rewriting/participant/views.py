from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from soutien_prog_back_rewriting.permissions import IsAuthenticatedWithJWTInCookie

from .models import Participant
from .serializers import ParticipantSerializer


class ParticipantViewSet(ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

    def get_permissions(self):
        permission_classes = []

        if self.action == "list" or self.action == "retrieve":
            permission_classes = [IsAuthenticatedWithJWTInCookie]

        return [permission() for permission in permission_classes]
