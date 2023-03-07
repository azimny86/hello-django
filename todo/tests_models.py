from django.test import TestCase
from .models import Item

class TestModels(TestCase):

    def test_done_defult_to_flase(self):
        item = Item.objects.create(name="Test Todo Item")
        self.assertFalse(item.done)