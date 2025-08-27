from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User

class CommentSerializer(serializers.ModelSerializer):
    # Relations Serializer 
    post = serializers.CharField(source="post.title", read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'text', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    # author = serializers.CharField(source='author.username', read_only=True)
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    # Nested Serializer
    comments = CommentSerializer(many=True, read_only=True)

    # MethodField Serializer
    comment_count = serializers.SerializerMethodField()  
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at', 'comments', 'comment_count']

    # MethodField
    def get_comment_count(self, obj):
        return obj.comments.count()

 # Subclasses Serializer 
class PostDetailSerializer(PostSerializer):
    comments = serializers.StringRelatedField(many=True)

    class Meta(PostSerializer.Meta):
        fields = PostSerializer.Meta.fields + ['comments']

# Aggregated API data
class PostStatsSerializer(serializers.Serializer):
    total_posts = serializers.IntegerField()
    total_comments = serializers.IntegerField()
    avg_comments_per_post = serializers.FloatField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']