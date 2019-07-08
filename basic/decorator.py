def login(func):
    def wrapper(*args, **kwargs):
        user = "abc"
        passwd = "123"
        username = input("account：")
        password = input("password：")
        if username == user and password == passwd:
            return func(*args, **kwargs)
        else:
            print("sorry,try again!")
    return wrapper


# 注意：使用装饰器必须要将@ + 完善函数放在待完善函数的定义前一行，等价于learning = login(learning)
@login
def learning():
    print("Welcome Learning Python")
learning()