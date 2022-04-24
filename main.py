from volt import *
if __name__ == "__main__":
    welcome_msg="""
    Welcome to Password manager
    """
    print(f"{welcome_msg:^500.upper()}")
    while True:
        account_name,username,password = "ACCOUNT NAME", "USERNAME", "PASSWORD"
        print(f"|{account_name:20} |{username:20} |{password:20}")
        for i,j in Credentials.password_vault.items():
            for k,l in j.items():
                print(f"|{i:20} |{k:20} |{l:20}")
                
        break 