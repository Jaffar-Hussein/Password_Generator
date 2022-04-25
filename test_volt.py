import unittest
from volt import *


class VoltTest(unittest.TestCase):
    """
    Tests for the volt module with the the two classes User and Credentials
    and all their methods
    """

    def setUp(self):
        """
        Runs before the test cases to initialize the different parameters to
        be tested
        """
        self.new_credential = Credentials('instagram', '123456', 'hanush')
        self.value_returned = Credentials.delete_credential('instagram')
        self.length_dictionary = len(Credentials.password_vault)
        self.display_dict = Credentials.display_credentials()
        self.new_user = User('hanan', 'jaffar')
        self.authenticate_false = User.authenticate('hanan', 'hussein')
        self.authenticate_true = User.authenticate('hanan', 'jaffar')
        self.auto_generated_password = Credentials.auto_generate_password(9)

    def test_credentials(self):
        """
        Checks if the credentials class is creating instances of new credentials
        """
        self.assertTrue(isinstance(self.new_credential, Credentials))

    def test_deletion_of_credentials(self):
        """
        Checks if the credentials can be deleted as the function returns the account name
        and not False
        and also checking if the dictionary holding accounts is empty 
        """
        self.assertTrue(self.value_returned)
        self.assertEqual(self.length_dictionary, 0)

    def test_display(self):
        """
        Checks if the display_credentials class returns a dictionary for the list of credentials
        """
        self.assertisNotNone(self.display_dict)

    def test_User(self):
        """
        Checks if the User class creates an instance when called with the details of 
        a user
        """
        self.assertTrue(isinstance(self.new_user, User))

    def test_authentiacate(self):
        """
        Tests whether the user authentification works correctly
        with both instances of a failed login attempt and successfull
        """
        self.assertFalse(self.authenticate_false)
        self.assertTrue(self.authenticate_true)

    def test_auto_generation(self):
        """
        Test to see if the length of the password auto generated is correct 
        Hence the password auto generation function works
        """
        self.assertEquals(len(self.auto_generated_password), 9)


if __name__ == "__main__":
    unittest.main()
