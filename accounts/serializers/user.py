from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Read-only user serializer (used for /me, profile, etc.)
    """

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "photo",
            "is_verified",
            "is_first_login",
            "date_joined",
        )
        read_only_fields = fields
