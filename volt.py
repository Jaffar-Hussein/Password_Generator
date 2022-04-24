
from password_generator import PasswordGenerator


class Credentials:
    """
    it creates credentials account which takes account name ,username and password
    """
    password_vault = {}

    def __init__(self, account_name, password, username):
        """
        initialize credentials

        Args:
            account_name (str): account name
            password (str): takes account password
            username (str): username used in the account
        """
        self.account_name = account_name
        self.password = password
        self.username = username
        Credentials.password_vault[account_name] = {username: password}

    @classmethod
    def delete_credential(cls, account_name):
        """deletes a user by account name

        Args:
            account_name (str): _description_

        Returns:
            _type_: _description_
        """
        return cls.password_vault.pop(account_name, "The account does not exist")

    @classmethod
    def display_credentials(cls):
        """
        Display all the credentials the user has access to

        Returns:
            dict: a collection of all the credentials the user has access to
        """
        return cls.password_vault

    @staticmethod
    def auto_generate_password(length):
        """
            Generates a new password using the auto generator
        Args:
            length (int): length of the password
        """
        return PasswordGenerator().non_duplicate_password(length)
class User:
    """
    creates a new user, and authenticates a user to the system
    """
    local_credentials=()
    def __init__(self,local_username,local_password):
        """initialize user

        Args:
            password (str): user password 
            username (str): username of the user
        """
        self.local_username= local_username
        self.local_password= local_password
        User.local_credentials=(local_username,local_password)
        
    @classmethod
    def authenticate(cls,username,password):
        """Authenticate user into the system

        Args:
            username (str): username to authenticate
            password (str): password to authenticate
        """
        if (username,password)==cls.local_credentials:
            return True
        return False


user1=User("jaffar","123456",)
print(user1.local_credentials)
print(user1.authenticate("hanan","23434554"))
print(user1.authenticate("jaffar","123456"))











cred1 = Credentials("insta", "100200", "jaffar")
# print(cred1.password_vault);
cred2 = Credentials("twitter", "00000007", "hanan")
# print(Credentials.password_vault)
# print(Credentials.delete_credential("twitter"))
# print(Credentials.password_vault)

print(Credentials.auto_generate_password(10))
# password_vault={
#     "insta":{
#         "jaffar":"1334"
#     }
# }
# print(Credentials.password_vault)

  
    