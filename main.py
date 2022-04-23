if __name__ == "__main__":
    welcome_msg="""
    Welcome to Password manger
    """
    print(welcome_msg)
    while True:
        account_name,username,password = "account_name", "username", "password"
        print(f"{account_name:} {username:10} {password:10}")
        for i,j in Credentials.password_vault.items():
            for k,l in j.items():
                print(f"{i:10} {k:10} {l:10}")