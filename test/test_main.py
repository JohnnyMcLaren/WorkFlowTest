from unittest import TestCase
from main import throwDice

class Test(TestCase):
    def test_throwDice(self):

        throw = throwDice(10)
        self.assertTrue(1 <= throw <= 10)
