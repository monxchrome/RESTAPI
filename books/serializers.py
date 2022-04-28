from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title']


class BookDetailSerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=3)
    class Meta:
        model = Book
        fields = '__all__'


