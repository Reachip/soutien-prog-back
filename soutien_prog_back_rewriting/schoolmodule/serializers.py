import re
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import SchoolModule


class SchoolModuleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SchoolModule
        fields = ("module_name", "id")

    def create(self, validated_data):
        if not re.match("^M[0-9]{4}", validated_data["module_name"]):
            raise ValidationError(
                "Mauvais format de nom de module. Le bon format serait par exemple : M2102"
            )

        return SchoolModule.objects.create(**validated_data)
