''' LOOP -- "FOR" "WHILE" 
for i in 'AJAY KUMAR' :
    print( i ) 
for i in [10,20,30,40,50] :
    print(i)
numbers = [1,2,3,4,5,6,7,8,9,10]
for n in numbers :
    if (n%2)==0:
        print(n,'is an even number')

print(list(range(10))) #or
d = list(range(10))
print(d)

for i in range(0,50) :
    if (i%2) == 0 :
        print(i)

n = int(input("start no. : "))
l = int(input("end no. : "))
while n <= l :
    print(n)
    n += 1
'''
n = int(input("Enter no. to get its factors : "))
print(1,end=" ")
f = 1
while f <= n/2 :
    f += 1
    if n % f ==0 :
        print(f,end=' ')
print(n)