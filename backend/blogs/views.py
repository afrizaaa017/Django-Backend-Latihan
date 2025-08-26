from rest_framework import viewsets
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, PostDetailSerializer, PostStatsSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count, Avg

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer

class PostDetailViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostDetailSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer

# Aggregated API data
class PostStatsView(APIView):
    def get(self, request):
        total_posts = Post.objects.count()
        total_comments = Post.objects.aggregate(total=Count('comments'))['total']
        avg_comments = Post.objects.annotate(num_comments=Count('comments')).aggregate(avg=Avg('num_comments'))['avg']

        data = {
            "total_posts": total_posts,
            "total_comments": total_comments,
            "avg_comments_per_post": avg_comments
        }
        return Response(PostStatsSerializer(data).data)

class UserPostListView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        return Post.objects.filter(author__username=username).order_by('-created_at')