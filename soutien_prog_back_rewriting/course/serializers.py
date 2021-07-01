from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Course
from schoolmodule.models import SchoolModule


class CourseSerializer(serializers.ModelSerializer):
    teacher = serializers.SlugRelatedField(
        many=False,
        read_only=False,
        slug_field='username',
        queryset=User.objects.all()
    )

    school_module = serializers.SlugRelatedField(
        many=False,
        read_only=False,
        slug_field='module_name',
        queryset=SchoolModule.objects.all()
    )

    class Meta:
        model = Course
        fields = ["id", "course_name", "description", "school_module", "teacher", "ending_at", "starting_at", "link_to"]

    def create(self, validated_data):
        starting_at, ending_at = (
            validated_data["starting_at"],
            validated_data["ending_at"],
        )

        if starting_at == ending_at:
            raise ValidationError("Les dates doivent être différentes")

        if starting_at > ending_at:
            raise ValidationError(
                "La date de début ne peut pas être supérieur à la date de fin. Les dates ont êtés inversées"
            )

        link = validated_data["link_to"]
        
        disc, zoom, teams, meet = (
            "https://discord.gg/",
            "https://us05web.zoom.us/",
            "https://teams.microsoft.com/",
            "https://meet.google.com/"
        )

        
        if not link.startswith(disc) and not link.startswith(zoom) and not link.startswith(teams) and not link.startswith(meet):
            raise ValidationError(
                "Lien vers la visioconférence invalide"
            )

        course_duration = (ending_at - starting_at).total_seconds() / 60

        if course_duration > 240:
            raise ValidationError("Un cours ne peut pas durer plus de quatre heures")

        return Course.objects.create(**validated_data)
