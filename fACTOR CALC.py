n = int(input("number : \n"))
i = 0
print("Factors : ",end="")
while i <= (n/2) :
    i += 1
    
    if n%i == 0 :
        print(i,end=",")
print(n)
print("DONE")
