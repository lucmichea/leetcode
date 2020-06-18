dict1 = {'a' : 1, 'b' : 2 , 'c' : 3}

#del(dict1['d']) # -> keyError
if 'c' in dict1:
    del(dict1['c'])

print(dict1)