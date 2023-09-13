"""EX01 - Chardle."""
__author__ = "730564969"

guess: str = input("Enter a 5-character word: ")
if len(guess) != 5: 
    print("Error: Word must contain 5 characters")
    exit()
character: str = input("Enter a single character: ")
if len(character) != 1:
    print("Error: Character must be a single character")
    exit()
instances: int = 0

print("Searching for " + character + " in " + guess)
if character == guess[0]:
    print(character + " found at index 0")
    instances = instances + 1
if character == guess[1]:
    print(character + " found at index 1")
    instances = instances + 1
if character == guess[2]:
    print(character + " found at index 2")
    instances = instances + 1
if character == guess[3]:
    print(character + " found at index 3")
    instances = instances + 1
if character == guess[4]:
    print(character + " found at index 4")
    instances = instances + 1

if instances == 0:
    print("No instances of " + character + " found in " + guess)
elif instances == 1:
    print("1 instance of " + character + " found in " + guess)
elif instances == 2:
    print("2 instances of " + character + " found in " + guess)
elif instances == 3:
    print("3 instances of " + character + " found in " + guess)
elif instances == 4:
    print("4 instances of " + character + " found in " + guess)
elif instances == 5:
    print("5 instances of " + character + " found in " + guess)
