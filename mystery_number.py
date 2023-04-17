"""This is one of the simple python projects for beginners but still the interesting one. In this project, we will create a program in which the system will choose a random number 
between any ranges defined, and then the user is given a hint to guess the number. Every time the user guesses the number wrongly, he is given another clue leading him toward the 
answer. The clue can be of any type like smaller, greater, multiples, dividers, etc. 

We will also need a function for checking whether the input is correct or not and to check the difference between the original number and the number guessed. """

import random

def random_num_generator():
    global x
    x = random.randint(1,10)
    print("The Mystery Number has been created!")

def number_picker():
    try:
        print("Pick a number from 1 to 10: ")
        response = int(input())

        if (response < x):
            print("The number you have guessed is lower than the Mystery Number. Try again!")
            number_picker()
        elif (response > x):
            print("The number you have guessed is greater than the Mystery Number. Try again!")
            number_picker()
        else:
            print("Congratulation! You guessed the Mistery Number! Do you want to play again? (Y/N)")
            play_again()     
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        number_picker()

def play_again():
    response_again = str(input()).upper()
    if(response_again == 'Y'):
            random_num_generator()
            number_picker()
    elif(response_again == 'N'):
        print("THE END")
    else:
        print("Please, type 'Y' if you want to play again, or 'N' if you wish to end the game.")
        play_again()

random_num_generator()
number_picker()



