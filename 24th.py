#FACTORIAL
# num = int(input("Enter number to get its factorial : "))
# j = 1
# for i in range (1,num+1) :
#     j *= i
#     i += 1
# print(j)


#AP
# def ap(a,n,d) :
#     val1 = (n/2)*(2*a+(n-1)*d)
#     return (val1)

# print("TO GET SUM OF AP PLS GIVE PARAMETERS : ")
# a = int(input("TYPE VALUE OF A : "))
# n = int(input("TYPE VALUE OF N : "))
# d = int(input("TYPE VALUE OF D : "))
# print(ap(a,n,d))

#GP
def gp(a,n,r) :
    if r > 1 :        
        val2 = a*((r**n)-1)/(r-1)
    if r < 1 :
        val2 = a*(1-(r**n))/(1-r)
    return (val2)

print("TO GET SUM OF GP PLS GIVE PARAMETERS : ")
a = int(input("TYPE VALUE OF A : "))
n = int(input("TYPE VALUE OF N : "))
r = float(input("TYPE VALUE OF R : "))
print(gp(a,n,r))
