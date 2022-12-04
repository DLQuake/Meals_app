from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    category = serializers.CharField(required=True)
    instructions = serializers.CharField(required=True)
    region = serializers.CharField(required=True)
    slug = serializers.SlugField(default = 'test')
    image_url = serializers.CharField(required=True)

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.category = validated_data.get('category', instance.category)
        instance.instructions = validated_data.get('instructions', instance.instructions)
        instance.region  = validated_data.get('region', instance.region)
        instance.slug  = validated_data.get('slug', instance.slug)
        instance.image_url  = validated_data.get('image_url', instance.image_url)
        instance.save()
        return instance

    def validate_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Nazwa musi sie składać tylko z liter!",)
        return value