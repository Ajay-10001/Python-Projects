y = 5
z = 12
x = 7
def numadd5() :
    global x 
    x = y + 5
    z = x + y
    print(x,z)
print(y)
print(z)
print(x)
numadd5()
print(y)
print(z)
print(x)