#TRAFFIC LIGHT
def trafficsys() :
    color = str(input("ENTER ANY ONE OF 3 COLOUR \n RED -- GREEN -- YELLOW \n"))
    coltuple = ("RED","GREEN","YELLOW")
    if color not in coltuple :
        print("ENTER A VALID COLOUR NAME")
    else :
        val = light(color)
        if val == 0 :
            print("STOP OR YOU WILL DIE")
        elif val == 1 :
            print("WAIT A BIT,THEN U CAN GO SAFELY")
        elif val == 2 :
            print("YEAH BUDDY! YOU CAN GO NOW")
        else :
            print("IS THIS NONE VALUE")

def light(colour) :
    if colour == "RED" :
        return 0
    elif colour == "GREEN" :
        return 2
    elif colour ==  "YELLOW" :
        return 1
    else :
        return "LOCATE THIS ERROR TO UNDERSTAND"

trafficsys()