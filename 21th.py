n = int(input("YOUR MAX NO. TO CHECK PRIMES : "))
for i in range(2,n+1) :
    j = 2
    while (j <= (i/2)) :
        if (i%j == 0) :
            break
        j += 1
    if (j>i/j) :
        print (i,"is a prime number")
print("Bye Bye!!")