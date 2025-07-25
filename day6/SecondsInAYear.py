def isleap(year):
    if (year % 100 != 0 and year % 4 == 0 ) or year % 400 == 0:
        return True
    else:
        return False

def SecondsinDays(numberOfDays):
    return numberOfDays*24*60*60

userInput = int(input("Enter a year : "))
if isleap(userInput):
    print("No. of seconds =",SecondsinDays(366))
else:
    print("No. of seconds =",SecondsinDays(365))
