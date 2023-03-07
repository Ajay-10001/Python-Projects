#if elif else
age = int(input("ENTER AGE : "))
if age == 18 :
    print("Can't decide.Need skill test in person.")
elif age > 18 and age <= 100 :
    print("Eligible")
elif age > 100 :
    print("You are dead.")
elif age < 18 and age > 7 :
    print("Not eligible.")
else :
    print("Bye Kiddo!")