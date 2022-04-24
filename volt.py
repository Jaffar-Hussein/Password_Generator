from password_generator import PasswordGenerator


class Credentials:
    """_summary_
    """
    password_vault = {}

    def __init__(self, account_name, password, username):
        """_summary_

        Args:
            account_name (_type_): _description_
            password (_type_): _description_
            username (_type_): _description_
        """
        self.account_name = account_name
        self.password = password
        self.username = username
        Credentials.password_vault[account_name] = {username: password}
        # Credentials.password_vault[account_name][username]=password

    @classmethod
    def delete_credential(cls, account_name):
        """_summary_

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

  
    