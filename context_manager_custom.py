from dict import te

with te.a() as s:
    print(s)
    print('c')

print(s)
print(te.count())
print(te.b)