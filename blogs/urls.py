from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, PostDetailViewSet, PostStatsView
# from django.urls import path

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'post_commented_by', PostDetailViewSet, basename='post_detail')
router.register(r'comments', CommentViewSet, basename='comment')

# comment_list_create = CommentViewSet.as_view()
# urlpatterns = [
#     path('comments/', comment_list_create, name='comment-list-create'),
# ]

urlpatterns = router.urls
# urlpatterns += router.urls
