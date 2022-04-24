from volt import User, Credentials
from getpass import getpass
if __name__ == "__main__":
        # welcome_msg="""
    # Welcome to Password manager
    # """
    # color  = "\u001b[31m"
    # print(f"{welcome_msg:^500}", "\u001b[31m")
    # while True:
    #     account_name,username,password = "ACCOUNT NAME", "USERNAME", "PASSWORD"
    #     print(f"|{account_name:20} |{username:20} |{password:20}")
    #     for i,j in Credentials.password_vault.items():
    #         for k,l in j.items():
    #             print(f"|{i:20} |{k:20} |{l:20}")

    #     break
    # banner text
    bannner = "WELCOME TO PASSWORD LOCKER"
    print("\u001b[4m", f"{bannner:^1000}", "\u001b[0m", "\n")
    # Account activation
    input("Press enter to create an account with a username and password : ")
    print()
    user_username = input("USERNAME : ")
    print()
    user_password = getpass("PASSWORD : ")
    print()
    new_user = User(user_username, user_password)
    print("\u001b[32m", "ACCOUNT SUCCESSFULLY CREATED", "\u001b[0m")
    print()
    print("Login to Your Account :")
        # Account authentification
    while True:
        print()
        user_username_verification = input("USERNAME : ")
        print()
        user_password_verification = getpass("PASSWORD : ")
        print()
        authentification = new_user.authenticate(
            user_username_verification, user_password_verification)
        if authentification:
            print("\u001b[32m", "SUCCESSFULL LOGIN", "\u001b[0m")
            print()
            break
        else:
            print("\u001b[31m", "WRONG CREDENTIALS\n", "\u001b[0m")
        print("TRY AGAIN")
           # Authentified user space
    user_options = {
        "0": "QUIT",
        "1": "Display Saved Credentials",
        "2": "Create New Credentials",
        "3": "Store an existing credentials",
        "4": "Delete a Credential"
    }
    new_credentials_options = {
        "y": "Auto Generated Password",
        "n": "Input Your Custom Password",
        "0": "Quit"
    }
    user_input = None
    main_menu_msg = "Main Menu "
    while user_input != "0":
        # Main Menu
        print(f"{main_menu_msg:^350}")
        for option, message in user_options.items():
            print(f"{option:^30} {message:<30}")
        # Options
        user_input = input(" : ")