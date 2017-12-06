Arr = []
print(Arr)

Arr.append('foo')
print(Arr)

Arr_2 = ['bar']
Arr.extend(Arr_2)
print(Arr)

Arr.insert(0, 'baz')
print(Arr)

Arr.remove('foo')
print(Arr)

i = Arr.index('baz')
print(i)
