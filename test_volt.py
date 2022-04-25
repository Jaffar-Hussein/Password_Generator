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
        self.new_user = User('hanan', 'jaffar')
        self.authenticate_false = User.authenticate('hanan', 'hussein')
        self.authenticate_true = User.authenticate('hanan', 'jaffar')
        self.auto_generated_password = Credentials.auto_generate_password(9)

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
