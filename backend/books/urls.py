from rest_framework.routers import DefaultRouter
from .views import BookListView, BookDetailView, BookAddView, BookDeleteView, BookUpdateView
from django.urls import path

# router = DefaultRouter()
# router.register(r"books", BookViewSet, basename="book")

# urlpatterns = router.urls

urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
    path('<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('create', BookAddView.as_view(), name='book-add'),
    # path('<str:book_title>', BookDetailView.as_view(), name='book-detail'),
    path('update/<int:pk>', BookUpdateView.as_view(), name='book-update'),
    path('delete/<int:pk>', BookDeleteView.as_view(), name='book-delete'),
]
