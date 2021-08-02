from django.db import models
from uuid import uuid4

# Abstract models


class UUIDModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )

    class Meta:
        abstract = True

# Create your models here.


class Writer(UUIDModel):
    name = models.CharField(
        verbose_name='Writer\'s name',
        max_length=100
    )

    def __str__(self):
        return self.name


class Book(UUIDModel):
    author = models.ForeignKey(
        to=Writer,
        on_delete=models.CASCADE,
        db_column='author_id',
        related_name='books'
    )

    name = models.CharField(
        verbose_name='Name of the book',
        max_length=100
    )

    def __str__(self):
        return f'{self.name} by {self.author}'
