f = open('foo', 'w')
try:
    f.write('Hora! We opened this file')
finally:
    f.close()
