from django.test import TestCase
from .models import Category
from random import seed
from random import randint

# Nekaj sem ekperimentrial (ne zmeni se na to)
class SettlementTypeModelTests(TestCase):

    def test_upper_limit_bigger_than_lower_limmit(self):
        seed(1)

        upperlimit = randint(0, 100000)
        category = Category(lowerLimit=upperlimit + 1000, upperLimit=upperlimit)

        def difference_positive(upperlim, lowerlim):
            boolean = True
            if (upperlim - lowerlim) < 0:
                boolean = False

            return boolean

        self.assertIs(difference_positive(category.upperLimit, category.lowerLimit), False)
