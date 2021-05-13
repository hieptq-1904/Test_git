def c(*args, **kwargs):
    print(kwargs)

a = {
    'a': 1,
    'b': 2
}
c(**a)