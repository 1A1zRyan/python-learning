import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """test for name_function.py"""

    def test_frist_last_name(self):
        formatted = get_formatted_name('Santiago', 'Chile')
        self.assertEqual(formatted, 'Santiago,Chile')

    def test_frist_middle_last_name(self):
        formatted = get_formatted_name('Santiago', 'Chile', 300000)
        self.assertEqual(formatted, 'Santiago,Chile-Population: 300000')

unittest.main()