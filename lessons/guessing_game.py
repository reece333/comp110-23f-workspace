"""Program that loops until correct number is guessed"""

from random import randint

secret: int = randint(1,10)
guess: int = int(input("Guess a number between 1 and 10: "))
number_of_tries: int = 1
max_tries: int =3

while (guess != secret) and (number_of_tries < max_tries):
    print("Wrong!")
    # If guess is out of bounds, tell them
    if(guess < 1 or guess > 10):
        print("Guess is not between 1 and 10, bozo.")
    # If guess is too low, tell them
    if guess < secret: 
        print("Too low!")
    # If guess is too high, tell them
    elif guess > secret:
        print("Too high!")
    print("You have " + str(max_tries - number_of_tries) + " attempts remaining!")
    # Ask for another guess
    guess = int(input("Guess again: "))
    number_of_tries += 1
    
if guess == secret:
    print("You guessed correctly!")
else:
    print("You lose!!!!! hahahahaha")