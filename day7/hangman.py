import random
import hangman_game


def printlives(lives):
    print(f"*********************************{lives}/6 LIVES LEFT*********************************")

def printstages(lives):
    print(hangman_game.stages[lives])



# word = random.choice(hangman_game.word_list)
word = "banana"
guessed_letters = ""
guessed_word = "_"*len(word)
lives = 6
guessed = False
while lives!=0 and guessed == False:
    print(f"The word is {guessed_word}")
    char = input("Enter a letter: ")
    guessed_word =""
    guessed_letters += char
    for letter in word:
        if letter in guessed_letters:
            guessed_word += letter
        else:
            guessed_word +="_"
    if guessed_word == word:
            guessed = True
    if char not in word:
        print(f"You guessed {char}, it was not in the word, you lost one life.")
        lives = lives - 1
    printstages(lives)
    printlives(lives)

if not guessed:
    print("Game over.")
else:
    print("You guessed the word!!")
print(f"The word was {word}")






