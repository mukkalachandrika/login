att=0
def dec1(func):
    def wrapper(*args,**kwargs):
        global att
        att=att+1
        func(*args,**kwargs)
    return wrapper
@dec1
def login(username,password):
    print("Login attempted by",username)
    