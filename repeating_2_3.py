dict = {'Russia': 'Moscow', 'China': 'Beijing', 'USA': 'Washington'}

print(dict.values())

print(dict.keys())

print(dict.items())

dict_2 = {'France': 'Paris'}

dict.update(dict_2)

print(dict)

print('France' in dict)

for i in dict:
    print(i, dict[i])
