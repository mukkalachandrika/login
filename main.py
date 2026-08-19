us = "chandrika"
ps = "chandrika@08"

def decl1(func):
    def wrapper(*args, **kwargs):
        print("Login successful")
        func(*args, **kwargs)
        print("Login successful")
    return wrapper

@decl1
def login(username, password):
    global us, ps

    if us == username and ps == password:
        print("Valid username and password")
    else:
        print("Invalid username or password")

login("chandrika", "chandrika@08")