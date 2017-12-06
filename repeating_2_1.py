dict_1 = {}
dict_2 = dict()
dict_3 = dict(dict_1)

print(dict_1 is dict_2)
print(dict_2 is dict_3)
print(dict_1 is dict_3)
