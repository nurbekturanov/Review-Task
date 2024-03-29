from rest_framework import serializers
from .models import User, Review, ReviewLike, Reply


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("id", "username", "full_name")

    def get_full_name(self, obj):
        return obj.get_full_name()


class ReviewLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewLike
        fields = ("id", "created_at")


class ReplySerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Reply
        fields = ("id", "author", "content", "parent_reply", "created_at")


class ReviewSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    likes_count = serializers.SerializerMethodField()
    reply_count = serializers.SerializerMethodField()
    last_five_replies = serializers.SerializerMethodField()

    def get_last_five_replies(self, obj):
        return ReplySerializer(obj.replies.order_by("-created_at")[:5], many=True).data

    class Meta:
        model = Review
        fields = (
            "id",
            "name",
            "author",
            "comment",
            "created_at",
            "likes_count",
            "reply_count",
            "last_five_replies",
        )

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_reply_count(self, obj):
        return obj.replies.count()
