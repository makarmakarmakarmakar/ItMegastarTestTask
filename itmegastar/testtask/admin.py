from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Writer)
class WriterAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    pass
