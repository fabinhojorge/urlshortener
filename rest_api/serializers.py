from rest_framework import serializers
from rest_api.models import Url


class UrlSerializer(serializers.Serializer):
    link = serializers.CharField(required=True, max_length=1000)
    link_short = serializers.CharField(read_only=True, max_length=100)
    count_request = serializers.IntegerField(read_only=True, default=1)
    count_clicked = serializers.IntegerField(read_only=True, default=0)

    @staticmethod
    def increment_count(value):
        return value + 1

    def create(self, validated_data):
        return Url.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.increase_count_request()
        instance.save()
        return instance
