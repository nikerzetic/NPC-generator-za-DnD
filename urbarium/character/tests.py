from django.test import TestCase
from django.core.validators import ValidationError

from .models import Character

class CharacterModelTests(TestCase):

    def test_abilities_in_range(self):
        """
        Ability values of Character class between 1 and 30
        """
        for x in [0,31]:
            for ability in ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']:
                with self.assertRaises(ValidationError):
                    test = Character(name='Test %s' %ability)
                    setattr(test, ability, x)
                    test.save()
