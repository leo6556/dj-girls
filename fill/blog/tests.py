from django.test import TestCase

# Create your tests here.
from .models import liki


class MyFirstTest(TestCase):

    def setUp(self):
        liki.objects.create(name='lool')

    def test_check(self):
        post = liki.objects.get(pk=1)
        excpected = f'{post.name}'
        self.assertEqual(excpected, 'lool')

