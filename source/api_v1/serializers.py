from rest_framework import serializers
# from webapp.models import Quote
from webapp.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Comment
        fields = ('text', 'photo', 'author', 'created_at')


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('photo', 'user')


# class QuoteUpdateSerializer(serializers.ModelSerializer):
#     created_at = serializers.DateTimeField(read_only=True)
#     author_name = serializers.CharField(read_only=True)
#     author_email = serializers.EmailField(read_only=True)
#
#     class Meta:
#         model = Quote
#         fields = ('id', 'text', 'created_at', 'status', 'author_name', 'author_email', 'rating')
#
#
# class QuoteRatingSerializer(serializers.ModelSerializer):
#     created_at = serializers.DateTimeField(read_only=True)
#     author_name = serializers.CharField(read_only=True)
#     author_email = serializers.EmailField(read_only=True)
#     status = serializers.CharField(read_only=True)
#     text = serializers.CharField(read_only=True)
#
#     class Meta:
#         model = Quote
#         fields = ('id', 'text', 'created_at', 'status', 'author_name', 'author_email', 'rating')