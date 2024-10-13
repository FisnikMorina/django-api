"""
Sample tests
"""

from django.test import SimpleTestCase

from app.calculate import add, subtract 

class CalcTests(SimpleTestCase):
    """Test the calculate module."""

    def test_add_numbers(self):
        """Test if calculate.add works."""
        result = add(5, 11)
        self.assertEqual(result, 16)

    def test_subtract_numbers(self):
        """Subtract x from y"""
        result = subtract(10, 15)
        self.assertEqual(result, 5)