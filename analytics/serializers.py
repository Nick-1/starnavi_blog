from rest_framework import serializers
from posts.models import Like


class LikeListSerializer(serializers.ModelSerializer):
    day = serializers.DateField()
    count = serializers.IntegerField()

    class Meta:
        model = Like
        fields = ['day', 'count']
