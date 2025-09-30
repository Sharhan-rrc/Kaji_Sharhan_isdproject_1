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
        self.default_client = Client(
            1001, "Alice", "Smith", "alice@pixell.com"
        )

    def test_attributes_set_correctly(self):
        """
        Tests that the Client instance attributes are set correctly.
        """
        self.assertEqual(
            self.default_client._Client__client_number, 1001
        )
        self.assertEqual(
            self.default_client._Client__first_name, "Alice"
        )
        self.assertEqual(
            self.default_client._Client__last_name, "Smith"
        )
        self.assertEqual(
            self.default_client._Client__email_address,
            "alice@pixell.com"
        )

    def test_invalid_client_number_raises_exception(self):
        """
        Tests that an invalid client number raises a ValueError.
        """
        with self.assertRaises(ValueError):
            Client("not-an-int", "Alice", "Smith", "alice@pixell.com")

    def test_blank_first_name_raises_exception(self):
        """
        Tests that a blank first name raises a ValueError.
        """
        with self.assertRaises(ValueError):
            Client(1002, "   ", "Smith", "alice@pixell.com")

    def test_blank_last_name_raises_exception(self):
        """
        Tests that a blank last name raises a ValueError.
        """
        with self.assertRaises(ValueError):
            Client(1003, "Alice", "   ", "alice@pixell.com")

    def test_invalid_email_sets_default(self):
        """
        Tests that an invalid email sets the default email address.
        """
        client = Client(1004, "Alice", "Smith", "invalid-email")
        self.assertEqual(
            client._Client__email_address, "email@pixell-river.com"
        )

    def test_client_number_property(self):
        """
        Tests the client_number property.
        """
        client = Client(1005, "Bob", "Jones", "bob@pixell.com")
        self.assertEqual(client.client_number, 1005)

    def test_first_name_property(self):
        """
        Tests the first_name property.
        """
        client = Client(1006, "Bob", "Jones", "bob@pixell.com")
        self.assertEqual(client.first_name, "Bob")

    def test_last_name_property(self):
        """
        Tests the last_name property.
        """
        client = Client(1007, "Bob", "Jones", "bob@pixell.com")
        self.assertEqual(client.last_name, "Jones")

    def test_email_address_property(self):
        """
        Tests the email_address property.
        """
        client = Client(1008, "Bob", "Jones", "bob@pixell.com")
        self.assertEqual(client.email_address, "bob@pixell.com")

    def test_str_method_format(self):
        """
        Tests the string representation of the Client instance.
        """
        client = Client(1009, "Charlie", "Brown", "charlie@pixell.com")
        expected = (
            "Brown, Charlie [1009] - charlie@pixell.com\n"
        )
        self.assertEqual(str(client), expected)


if __name__ == "__main__":
    unittest.main()