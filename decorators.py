def my_deco(func):
    def wrapper():
        print("Before Function")
        func()
        print("after function")
    return wrapper    