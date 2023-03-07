# def cube(n) :
#     print ("ID OF VARIABLE BEFORE CHANGE : ",id(n),"Value : ",n)
#     n **= 3
#     print ("ID OF VARIABLE AFTER CHANGE : ",id(n),"Value : ",n)
#     return("Return statement with value",n)
# test = 2
# print(id(test))
# print(cube(test))

# def alno(TEST) :
#     COUNT = 0
#     for i in TEST :
#         COUNT += 1
#     return("NUMBER OF ALPHABETS :",COUNT)
    
# str1 = str(input("TYPE YOUR ALPHABETS HERE : \n"))
# print("\n",str1)
# print(alno(str1))

#works only for mixed fraction

def mix(num,deno = 1) :
    rema = num % deno
    if rema != 0 :
        quot = num//deno
        print("YOUR INPUT",int(num),"/",int(deno),"\nYOUR RESULT",int(quot),"(",int(rema),"/",int(deno),")")
    else :
        print("YOUR INPUT LEADS TO AN INTEGER NOT A MIXED FRACTION")

NUM = float(input("NUMERATOR : "))
DENO = float(input("DENOMINATOR : "))
CHECK = NUM/DENO
if CHECK >= 1 :
    mix(NUM,DENO)
else :
    print("YOU GAVE AN INPUT FOR PROPER FRACTION")

