"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal, run:
    python -m unittest tests/test_client.py
"""

import unittest
from client.client import Client


class TestClient(unittest.TestCase):
    """
    Unit tests for the Client class.
    """

    def setUp(self):
        """
        Sets up a common Client instance for reuse in tests.
        """
        self.valid_client = Client(1001, "Alice", "Smith", "alice@pixell.com")

    def test_valid_attributes_set_correctly(self):
        """
        Tests that the Client instance attributes are set correctly with valid input.
        """
        self.assertEqual(self.valid_client.client_number, 1001)
        self.assertEqual(self.valid_client.first_name, "Alice")
        self.assertEqual(self.valid_client.last_name, "Smith")
        self.assertEqual(self.valid_client.email_address, "alice@pixell.com")

    def test_invalid_client_number_raises_exception(self):
        """
        Tests that an invalid client number raises a ValueError exception.
        """
        with self.assertRaises(ValueError):
            Client("invalid", "Alice", "Smith", "alice@pixell.com")

    def test_blank_first_name_raises_exception(self):
        """
        Tests that a blank first name raises a ValueError exception.
        """
        with self.assertRaises(ValueError):
            Client(1001, "", "Smith", "alice@pixell.com")

    def test_blank_last_name_raises_exception(self):
        """
        Tests that a blank last name raises a ValueError exception.
        """
        with self.assertRaises(ValueError):
            Client(1001, "Alice", "", "alice@pixell.com")

    def test_invalid_email_sets_default(self):
        """
        Tests that an invalid email address sets the default email value.
        """
        client = Client(1001, "Alice", "Smith", "invalid-email")
        self.assertEqual(client.email_address, "email@pixell-river.com")

    def test_client_number_property(self):
        """
        Tests that the client_number property returns the correct value.
        """
        self.assertEqual(self.valid_client.client_number, 1001)

    def test_first_name_property(self):
        """
        Tests that the first_name property returns the correct value.
        """
        self.assertEqual(self.valid_client.first_name, "Alice")

    def test_last_name_property(self):
        """
        Tests that the last_name property returns the correct value.
        """
        self.assertEqual(self.valid_client.last_name, "Smith")

    def test_email_address_property(self):
        """
        Tests that the email_address property returns the correct value.
        """
        self.assertEqual(self.valid_client.email_address, "alice@pixell.com")

    def test_string_method_format(self):
        """
        Tests that the __str__ method returns the correctly formatted string.
        """
        expected = "Smith, Alice [1001] - alice@pixell.com\n"
        self.assertEqual(str(self.valid_client), expected)


if __name__ == "__main__":
    unittest.main()