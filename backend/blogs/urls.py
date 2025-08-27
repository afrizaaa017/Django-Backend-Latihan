from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, PostDetailViewSet, PostStatsView, UserPostListView, UserListView
from django.urls import path, include

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'post_commented_by', PostDetailViewSet, basename='post_detail')
router.register(r'comments', CommentViewSet, basename='comment')

# comment_list_create = CommentViewSet.as_view()
# urlpatterns = [
#     path('comments/', comment_list_create, name='comment-list-create'),
# ]

# urlpatterns += router.urls
urlpatterns = [
    path('', include(router.urls)),
    path('<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('users/list', UserListView.as_view(), name='user-list'),
]