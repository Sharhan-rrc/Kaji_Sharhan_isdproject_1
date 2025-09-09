"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""
import unittest
from client.client import Client

class TestClient(unittest.TestCase):

    def test_attributes_set_correctly(self):
        client = Client(1001, "Alice", "Smith", "alice@pixell.com")
        self.assertEqual(client._Client__client_number, 1001)
        self.assertEqual(client._Client__first_name, "Alice")
        self.assertEqual(client._Client__last_name, "Smith")
        self.assertEqual(client._Client__email_address, "alice@pixell.com")

    def test_invalid_client_number_raises_exception(self):
        with self.assertRaises(ValueError):
            Client("not-an-int", "Alice", "Smith", "alice@pixell.com")

    def test_blank_first_name_raises_exception(self):
        with self.assertRaises(ValueError):
            Client(1002, "   ", "Smith", "alice@pixell.com")

    def test_blank_last_name_raises_exception(self):
        with self.assertRaises(ValueError):
            Client(1003, "Alice", "   ", "alice@pixell.com")

    def test_invalid_email_sets_default(self):
        client = Client(1004, "Alice", "Smith", "invalid-email")
        self.assertEqual(client._Client__email_address, "email@pixell-river.com")

    def test_client_number_property(self):
        client = Client(1005, "Bob", "Jones", "bob@pixell.com")
        self.assertEqual(client.client_number, 1005)

    def test_first_name_property(self):
        client = Client(1006, "Bob", "Jones", "bob@pixell.com")
        self.assertEqual(client.first_name, "Bob")

    def test_last_name_property(self):
        client = Client(1007, "Bob", "Jones", "bob@pixell.com")
        self.assertEqual(client.last_name, "Jones")

    def test_email_address_property(self):
        client = Client(1008, "Bob", "Jones", "bob@pixell.com")
        self.assertEqual(client.email_address, "bob@pixell.com")

    def test_str_method_format(self):
        client = Client(1009, "Charlie", "Brown", "charlie@pixell.com")
        expected = "Brown, Charlie [1009] - charlie@pixell.com\n"
        self.assertEqual(str(client), expected)

if __name__ == "__main__":
    unittest.main()