n = 237
i = 11
print("Guess the no.")
while i > 0 :
    t = int(input("TYPE NUMBER : \n"))
    i -= 1
    if t < n :
        print("Nah,it is greater \n Chance(s) left ",i)
        continue
    if t > n :
        print("Nah, it is smaller \n Chance(s) left ",i)
        continue
    if t == n :
        print("Congratulations! You got it. \n Chance(s) left ",i)
        break
print("Thanks for wasting your time. :-)")