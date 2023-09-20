"""Exercise 2 - One Shot Wordle!!!!!!"""
__author__ = "730564969"

secret = str("python")
guess: str = input("What is your " + str(len(secret)) + "-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index: int = 0
emoji: str = ""
exists: bool = False
alt: int = 0

# Ensure guess is the correct length
while len(guess) != len(secret): 
    guess = input("That was not " + str(len(secret)) + " letters! Try again: ")

while index < len(guess):
    # Check for green box
    if guess[index] == secret[index]:
        emoji += GREEN_BOX
    # Check for white/yellow box
    if guess[index] != secret[index]:
        # Checking alt indices
        while exists is False and alt < len(guess):
            if guess[index] == secret[alt]:
                exists = True
            else:
                alt += 1
        # Index exists elsewhere, so append yellow box
        if exists is True:
            emoji += YELLOW_BOX
        # Neither the index or alternates match, so append white box
        if exists is False:
            emoji += WHITE_BOX
    # Increase index to avoid inf loop, reset alt & exists variables to properly evaluate other indices (probably not the best way to do this)
    index += 1
    alt = 0
    exists = False

print(emoji)
if guess != secret:   
    print("Not quite. Play again soon!")
if guess == secret:
    print("Woo! You got it!")