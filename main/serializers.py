from rest_framework import serializers
from main.models import Post, Like
from users.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CreateLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class ListLikeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    post = PostSerializer()

    class Meta:
        model = Like
        fields = '__all__'
