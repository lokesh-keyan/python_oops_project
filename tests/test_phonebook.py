import unittest
from UnitTesting.phonebook.phonebook import PhoneBook

class PhoneBookTest(unittest.TestCase):
    def test_lookup_by_name(self):
        phonebook = PhoneBook()
        phonebook.add("Bob", "12345")
        number = phonebook.lookup("Bob")
        self.assertEqual("12345", number)
