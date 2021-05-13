def deco(func):
    def wrapper(*args, **kwargs):
        print("This will get printed before the function is called.")
        func(*args, **kwargs)
        print("This will get printed after the function is called.")
        print(kwargs['b'])

    return wrapper


@deco
def c(**args, **kwargs):
    print('This print from function C')


c(a = 1, b = 2, c= 4)
