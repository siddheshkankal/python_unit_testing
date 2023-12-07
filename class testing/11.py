import unittest
from notebook import Note
 
 
class TestNote(unittest.TestCase):
    def test_note_has_category_class_attr(self):
        msg = 'The Note class does not have a CATEGORY attribute.'
        self.assertTrue(hasattr(Note, 'CATEGORY'), msg)