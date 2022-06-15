from django.test import TestCase
from guide.models import Dish

class DishTests(TestCase):
    def test_str(self):
        dish = Dish(dish_name='pelmen', cuisine='Russia')
        self.assertEquals(
            str(dish),
            'pelmen -- Russia',
        )
