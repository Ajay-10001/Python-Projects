'''
if and elif and else
n1 = int(input("NO. 1 : "))
n2 = int(input("NO. 2 : "))
if n1>n2 :
    diff = n1-n2
else :
    diff = n2-n1
print("The positive difference of",n1,"and",n2,"is",diff)

n1 = int(input("no. 1 : "))
n2 = int(input("no. 2 : "))
diff = n1-n2
if diff>0 :
    print("diff is positive",diff)
elif diff==0 :
    print("equal numbers",diff)
else :
    print("diff is negative",diff)
'''
res = 0
val1 = float(input("1st no.: "))
val2 = float(input("2nd no.: "))
op = input("Enter any one of the operator-(+,-,*,/) : ")
if op == "+" :
    res = val1+val2
elif op == "-" :
    if val1 > val2 :
        res = val1 - val2
    else :
        res = val2 - val1
elif op == "*" :
    res = val1*val2
elif op == "/" :
    if val2 == 0 :
        res = "ERROR CUZ DIVISIBILITY BY 0"
    else :
        res = val1/val2
else :
    res = ("WRONG INPUT AS OPERATOR")
print("THE RESULT IS :",res)
input("PRESS ANY KEY TO END")
