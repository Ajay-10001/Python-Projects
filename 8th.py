#STRINGS
#indexed from 0 to so on
# AJAY
#0=A,1=J,2=A,3=Y
a="AJAY KUmAR"
print(a[1:9])  # star from 1 but end before 9,9 is not included
print(len(a))
print(a.lower())
b=a.lower()
d=a.upper()
c=a[1:7]
print(b,c,d)
print(a.replace('A','L'))
print(a.split(" "))
print(a.split("A"))