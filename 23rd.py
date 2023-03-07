dict1 = {2:4,3:5,6:8}
print(dict1)
print(dict1.items())
for key in dict1 :
    print(key)
for val,key in dict1 :
    print(key)
for key in dict1.items() :
    print(key)
for val,key in dict1.items() :
    print(key)
for key,val in dict1.items() :
    print(key,val,end=" ")