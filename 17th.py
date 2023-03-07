#BREAK
''' n =str(30345467)
for i in n :
    if i == str(5) :
        print("error")
        break
    print(i)

n = 0
for n in range(20) :
    if n == 17 :
     print("17 encountered")
     break
    print(n)
'''
no = 0
sum = 0
while True:
    no = int(input())
    if no <= 0 :
        print("lol")
        break
    sum += no
    print("total",sum,"last added",no)
    