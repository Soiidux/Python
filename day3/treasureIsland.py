print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
)

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("You are at a crossroads. Do you want to go left (L) or right (R)? ")

if direction == "left" or direction == "L":
    lake = input("You come to a lake. There is an island in the middle of the lake. Do you wait(W) for a boat or swim(S) across? ")
    if lake == "wait" or lake == "W":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red (R), one yellow (Y) and one blue (B). Which door do you choose? ")
        if door == "yellow" or door == "Y":
            print("You found the treasure. Congratulations! But it is still - Game Over!")
        elif door == "red" or door == "R":
            print("The room was on fire and you were burnt alive. Game Over!")
        else:
            print("Blue beasts behind the door ate you alive. Game Over!")
    else:
        print("A giant trout ate you. Game Over!")
else:
    print("You fell into a hole and died. Game Over!")