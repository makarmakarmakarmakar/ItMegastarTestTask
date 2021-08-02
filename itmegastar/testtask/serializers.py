from rest_framework import serializers
from . import models


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ['id', 'name']


class WriterSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = models.Writer
        fields = ['id', 'name', 'books']
