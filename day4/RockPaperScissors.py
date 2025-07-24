from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hands = [rock,paper,scissors]

while True:
    try:
        userhand = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
        if 0<=userhand<=2:
            break
        else:
            print("Invalid input. Try again.")
    except:
        print("Invalid input. Try again.")

computerhand = randint(0,2)
print("You chose :")
print(hands[userhand])
print("*"*50)
print("The computer chose :")
print(hands[computerhand])

if (userhand == 0 and computerhand == 1) or (userhand == 1 and computerhand == 2) or (userhand == 2 and computerhand == 0):
    print("You lose.")
elif(userhand == computerhand):
    print("Its a tie.1"
          "")
else:
    print("You win.")