#Faulty calculator
#4+2= 12
#12/3= 56
#4*3= 128
n1 = int(input("1st no. : "))
n2 = int(input("2nd no. : "))
o1 = input("Any one of these operators : + - * / : ")
if n1 == 4 and n2 == 2 and  o1 == "+" :
    res = "12"
elif n1 == 12 and n2 == 3 and  o1 == "/" :
    res = "56"
elif n1 == 4 and n2 == 3 and  o1 == "*" :
    res = 128
elif o1 == "+" :
    res = n1 + n2
elif o1 == "-" :
    res = n1 - n2
elif o1 == "*" :
    res = n1 * n2
elif o1 == "/" :
    res = n1 / n2
else :
    res = "ERROR"
print(res)
               