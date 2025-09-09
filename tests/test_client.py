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

    def test_valid_client_initialization(self):
        client = Client(1010, "Susan", "Clark", "susanclark@pixell.com")
        self.assertEqual(client._Client__client_number, 1010)
        self.assertEqual(client._Client__first_name, "Susan")
        self.assertEqual(client._Client__last_name, "Clark")
        self.assertEqual(client._Client__email_address, "susanclark@pixell.com")

    def test_invalid_client_number_type(self):
        with self.assertRaises(ValueError) as context:
            Client("1010", "Susan", "Clark", "susanclark@pixell.com")
        self.assertIn("Client number must be an integer", str(context.exception))

    def test_blank_first_name(self):
        with self.assertRaises(ValueError) as context:
            Client(1010, "   ", "Clark", "susanclark@pixell.com")
        self.assertIn("First name cannot be blank", str(context.exception))

    def test_blank_last_name(self):
        with self.assertRaises(ValueError) as context:
            Client(1010, "Susan", "   ", "susanclark@pixell.com")
        self.assertIn("Last name cannot be blank", str(context.exception))

    def test_invalid_email_address_fallback(self):
        client = Client(1010, "Susan", "Clark", "not-an-email")
        self.assertEqual(client._Client__email_address, "email@pixell-river.com")

    def test_str_representation(self):
        client = Client(1010, "Susan", "Clark", "susanclark@pixell.com")
        expected = "Clark, Susan [1010] - susanclark@pixell.com\n"
        self.assertEqual(str(client), expected)

if __name__ == "__main__":
    unittest.main()