from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView

# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all().order_by("-id")
#     serializer_class = BookSerializer

# List semua buku
class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Detail 1 buku
class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # lookup_field = 'title'
    # lookup_url_kwarg = 'book_title

# Tambah buku 
class BookAddView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Edit buku 
class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Hapus buku
class BookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer