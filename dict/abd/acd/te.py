class a(object):
    def __enter__(self):
        print('sss')
        return 'sss111'
    def __exit__(self ,type, value, traceback):

        return False

b =4
c = 5
def count():
    return 5