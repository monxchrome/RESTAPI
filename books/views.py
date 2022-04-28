from rest_framework import generics, permissions
from .serializers import BookSerializer, BookDetailSerializer
from .models import Book
from .pagination import StandardResultsSetPagination


class BooksListView(generics.ListAPIView):
    """
    Is ***comment***
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = StandardResultsSetPagination


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    permission_classes = [permissions.IsAdminUser]


class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAdminUser]


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    permission_classes = [permissions.IsAdminUser]
