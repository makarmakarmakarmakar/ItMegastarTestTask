from django.test import TestCase
from . import models
from rest_framework.reverse import reverse
from rest_framework import status

# Create your tests here.


class WriterTest(TestCase):
    def setUp(self):
        models.Writer.objects.create(name='Vladimir Nabokov')  # 0 книг

        pushkin = models.Writer.objects.create(name='Alexander Pushkin')  # 1 книга
        models.Book.objects.create(name='Eugene Ongene', author=pushkin)

        solzhenitsyn = models.Writer.objects.create(name='Alexander Solzhenitsyn')  # 2 книги
        models.Book.objects.create(name='The Gulag archipelago', author=solzhenitsyn)
        models.Book.objects.create(name='One day in the life of Ivan Denisovich', author=solzhenitsyn)

    def test_list(self):
        """
        Проверка получения информации о писателях и их книгах.
        """
        url = reverse('testtask:writers-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_retrieve(self):
        """
        Проверка получения информации о конкретном писателе и о его книгах.
        """
        solzhenitsyn = models.Writer.objects.get(name='Alexander Solzhenitsyn')

        url = reverse('testtask:writers-detail', kwargs={"pk": str(solzhenitsyn.id)})
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], str(solzhenitsyn.id))
        self.assertEqual(len(response.data['books']), 2)


