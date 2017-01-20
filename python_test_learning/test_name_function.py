import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """test for name_function.py"""

    def test_frist_last_name(self):
        formatted = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted, 'Janis Joplin')

unittest.main()