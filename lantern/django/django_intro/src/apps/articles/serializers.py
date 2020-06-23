from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    body = serializers.CharField(max_length=500)
    tags = serializers.CharField(max_length=10)
    author = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.tags = validated_data.get('tags', instance.tags)
        instance.author_id = validated_data.get('author_id', instance.author_id)
        instance.save()

        return instance
