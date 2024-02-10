from django.test import TestCase

from item.logic import operations


class LogicTestCase(TestCase):
    def test_plus(self):
        result = operations(5, 13, '+')
        self.assertEqual(18, result)

    def test_minus(self):
        result = operations(6, 13, '-')
        self.assertEqual(-7, result)

    def test_multiply(self):
        result = operations(5, 13, '*')
        self.assertEqual(65, result)

    def test_divide(self):
        result = operations(26, 13, '/')
        self.assertEqual(2, result)
