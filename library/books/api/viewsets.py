from rest_framework import viewsets

from library.books import models
from library.books.api import serializers


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BookSerializer
    queryset = models.Book.objects.all()
