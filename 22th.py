no = int(input("your number : "))
for i in range(2,no+1) :
    j = 2
    while j <= (i/2) :
        if (i%j)==0 :
            print(i,"is not a prime")
            break
        j += 1
    if j > (i/2) :
            print(i,"is a prime")
print("done")

