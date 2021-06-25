from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    teacher = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='username'
    )

    school_module = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='module_name'
    )

    class Meta:
        model = Course
        fields = ["description", "school_module", "teacher", "ending_at", "starting_at"]

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

        course_duration = (ending_at - starting_at).total_seconds() / 60

        if course_duration > 240:
            raise ValidationError("Un cours ne peut pas durer plus de quatre heures")

        return Course.objects.create(**validated_data)
