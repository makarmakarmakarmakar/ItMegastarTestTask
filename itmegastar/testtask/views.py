from rest_framework import viewsets
from . import models, serializers
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

# Create your views here.


class WriterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Writer.objects.all()
    serializer_class = serializers.WriterSerializer

    # Инструмент, позволяющий кэшировать данные (60 * 15 = 15 минут),
    # снижающий число избыточных повторных обращений к БД
    @method_decorator(cache_page(60 * 15))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
