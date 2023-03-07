status = "Y"
while status == "Y" :
    print("This is prime number checker and list maker.")
    print("To check if a number is prime type - CHECK")
    print("To make a list of primes to a certain limit type - LIST")
    tpr = str(input())
    pr = tpr.upper()
    if pr == "CHECK" :
        n = int(input("Enter the number to check if it is prime or not. : \n"))
        i = 2
        while i <= (n/2) :
            if n%i == 0 :
                print(n,"is not a prime number.")
                break
            i += 1
        if i > (n/2) :
            print(n,"is a prime number.")
    elif pr == "LIST" :
        n = int(input("Enter the number to make list of primes till. : \n"))
        print("LIST STARTS HERE")
        c = 0
        for i in range(2,n+1) :
            j = 2
            while j <= (i/2) :
                if i%j == 0 :
                    break
                j += 1
            if j > (i/2) :
                c += 1
                print(i)
        print("Total prime numbers found =",c)
    else :
        print("WRONG INPUT")
    print("Do You Want to Re-run this program \n 'Y'for YES : 'N'for NO")
    statrecheck = str(input())
    status = statrecheck.upper()
print("Program ended.")


