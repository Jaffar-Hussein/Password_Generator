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
     # Display of available credentials
        if user_input == "1":
            account_name, username, password = "ACCOUNT NAME|", "USERNAME|", "PASSWORD|"
            print(f"\t|{account_name:20} |{username:20} |{password:20}")
            for i, j in Credentials.display_credentials().items():
                for k, l in j.items():
                    print()
                    print(f"\t {i:20}  {k:20}  {l}")
            print()
            input("Press Enter To Go Back to Main Menu.....")
            print()
     # Creation and saving of new credentials
        if user_input == "2":
            print()
            account_name_2 = input("Enter Account name : ")
            print()
            username_2 = input("Enter Username : ")
            print()
            print("Do you want an auto generated password : \n")
            for option, message in new_credentials_options.items():
                print(f"{option:^30} {message:<30}")
            print()
            user_input = input(" : ").casefold()
            if user_input == 'y':
                user_input = input(
                    " How long do you want the password to be ? : ")
                user_password2 = Credentials.auto_generate_password(
                    int(user_input))
            elif user_input == 'n':
                user_password2 = input("Input your own password : ")

            Credentials(account_name_2, user_password2, username_2)
            print("\u001b[32m",
                  "\t\tCREDENTIAL SUCCESSFULLY SAVED", "\u001b[0m")

            input("Press Enter To Go Back to Main Menu.....")
            print()
     # Storage of existing credentials
        if user_input == "3":
            print("Input the details below : ")
            account_name_3 = input("ACCOUNT NAME : ")
            user_username_3 = input("USERNAME : ")
            user_password_3 = input("PASSWORD : ")
            print()
            Credentials(account_name_3, user_password_3, user_username_3)
            print("\u001b[32m",
                  "\t\tCREDENTIAL SUCCESSFULLY SAVED", "\u001b[0m")

            input("Press Enter To Go Back to Main Menu.....")
            print()
    # Deletion of a credential
        if user_input == "4":
            print("Enter the account name you want to delete")
            user_input = input(" : ")
            deletion=Credentials.delete_credential(user_input)
            if deletion == False:
                print("\u001b[33m",
                  f"\t\tThe account you are trying to delete does not exist", "\u001b[0m")
            else:
                print("\u001b[32m",
                    f"\t\tThe {user_input} account has been deleted successfully", "\u001b[0m")

            input("Press Enter To Go Back to Main Menu.....")
            print()
    else:
        # Bye bye message
        print("\u001b[32m",
                    f"""\t\tYou've left our system ....... See you sooon
                                    Made with  ♥️ HJ 
                    """, "\u001b[0m")
