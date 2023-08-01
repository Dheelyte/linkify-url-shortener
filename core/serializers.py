from rest_framework import serializers
from .models import Link


class LinkSerializer(serializers.ModelSerializer):
    absolute_url = serializers.ReadOnlyField(source='get_absolute_url')
    short_link_id = serializers.CharField(allow_blank=True)
    class Meta:
        model = Link
        fields = ['link', 'short_link_id', 'absolute_url']