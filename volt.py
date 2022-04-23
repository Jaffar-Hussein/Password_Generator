from ast import Delete


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
            account_name (_type_): _description_

        Returns:
            _type_: _description_
        """
        return cls.password_vault.pop(account_name, "The account does not exist")


cred1 = Credentials("insta", "100200", "jaffar")
# print(cred1.password_vault);
cred2 = Credentials("twitter", "00000007", "hanan")
print(Credentials.password_vault)
print(Credentials.delete_credential("twitter"))
print(Credentials.password_vault)


# password_vault={
#     "insta":{
#         "jaffar":"1334"
#     }
# }
