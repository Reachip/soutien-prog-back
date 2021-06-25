from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Participant
from .serializers import ParticipantSerializer


class ParticipantViewSet(ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

    def get_permissions(self):
        permission_classes = []

        if self.action == "read":
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]
