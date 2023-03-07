# def perimeter(l,b) :
#     perim = 2*(l+b)
#     return(perim)

# l = int(input("length : "))
# b = int(input("breadth : "))
# res = perimeter(l,b)
# print(res)
str1 = "AJAY KUMAR"
list1 = ["lolu","golu","molu",17]
tuple1 = ("billa","lella",22)
set1 = {"hell","bell","kell",78}
dict1 = {1:"one",2:"two","lol":"gol","ten":10}
print(str1,"\n",list1,"\n",tuple1,"\n",set1,"\n",dict1)
print(str1[6])
print(list1[2])
print(tuple1[2])
print(set1[3])                  #a set is no indexed or sequenced,
           #so can't call a value from it until it is coverted tp list or tuple.
print(dict1["lol"])
