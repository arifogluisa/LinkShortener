from .models import Link
from rest_framework import serializers


class LinkSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model=Link
        fields='__all__'