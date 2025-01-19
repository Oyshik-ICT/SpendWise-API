from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Catagoery


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance:
            self.fields["password"].required = False

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))
        return super().update(instance, validated_data)


class CatagoerySerializer(serializers.ModelSerializer):
    total_expense = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Catagoery
        fields = (
            "id",
            "groceries",
            "leisure",
            "electronics",
            "utilities",
            "clothing",
            "health",
            "others",
            "user",
            "total_expense",
            "created_at",
        )
        extra_kwargs = {
            "user": {"read_only": True},
            "created_at": {"read_only": True},
            "total_expense": {"read_only": True},
        }

    def get_total_expense(self, obj):
        return (
            obj.groceries
            + obj.leisure
            + obj.electronics
            + obj.utilities
            + obj.clothing
            + obj.health
            + obj.others
        )

    def get_created_at(self, obj):
        return obj.created_at.date()
