#nested loop
'''
for ol in range(5) :
    print("--repeating times",ol+1,"outer loop")
    for il in range(3) :
        print("repeating times",il+1,"inner loop")
    print("out of inner loop for",ol+1,"time")
print("out of outer loop")
'''
no = int(input("Enter number to get a pattern : "))
for i in range(1,no+1) :
    for j in range (1,i+1) :
        print (j,"*",end=" ")
    print()