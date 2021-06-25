from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .models import Participant


class ParticipantSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Participant
        fields = ["course", "mail", "name"]

    def create(self, validated_data):
        return super().create(validated_data)
