#PRIME CHECKER
num = int(input("Enter no. to be checked : "))
flag = 0
if num > 4 :
    for i in range(2,int(num/2)) :
        if (num % i) == 0 :
            flag = 1
            break
    if flag == 1 :
        print(num,"is not a prime number")
    else :
        print(num,"is a prime number")
elif num == 4 :
    print(num,"is not a prime number")
elif num == 3 :
    print(num,"is a prime number")
elif num == 2 :
    print(num,"is a prime number")
else :
    print("Entered number is <=1,execute again")

