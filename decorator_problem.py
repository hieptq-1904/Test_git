def a():
    print("This will get printed before the function is called.")

def b():
    print("This will get printed after the function is called.")

def c():
    a()
    print('This print from function C')
    b()

c()
