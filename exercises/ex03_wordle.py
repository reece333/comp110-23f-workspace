"""Wordle."""
__author__ = "730564969"

def contains_char(search_str: str, target_char: str) -> bool:
    # Assert that target_char is a single character
    assert len(target_char) == 1
    # Initialize index
    index = 0
    # Iterate through characters of guess_string 
    while index < len(search_str):
        # Check if current character is equal to target_char
        if search_str[index] == target_char:
            return True
        # Increment index to move to next character
        index += 1
    # Didn't find the target_char, return False
    return False

def emojified(guess_str: str, secret_str: str) -> str:
    # Define emoji characters
    GREEN_BOX = "🟩"
    YELLOW_BOX = "🟨"
    WHITE_BOX = "⬜"
    # Create an emoji string based on guess and secret string
    assert len(guess_str) == len(secret_str)
    emoji_str: str = ""
    # Initialize index
    index = 0
    while index < len(guess_str):
        # Check for green box
        if guess_str[index] == secret_str[index]:
            emoji_str += GREEN_BOX
        else:
            # Check if the current character exists in secret_str
            if contains_char(secret_str, guess_str[index]):
                emoji_str += YELLOW_BOX
            else:
                emoji_str += WHITE_BOX 
        # Increment index to avoid an infinite loop
        index += 1
    return emoji_str

def input_guess(expected_length: int) -> str:
    while True:
        user_input = input("Enter a " + str(expected_length) + " character word: ")
        if len(user_input) == expected_length:
            return user_input
        else:
            print("That wasn't " + str(expected_length) + " chars! Try again: ")

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word = "codes"
    max_turns = 6
    turn = 1
    while turn <= max_turns:
        print("=== Turn " +  str(turn) + "/" + str(max_turns) + " ===")
        # Prompt user for a guess
        user_guess = input_guess(len(secret_word))
        # Get emoji results of user's guess versus secret
        emoji_result = emojified(user_guess, secret_word)
        # Print resulting string
        print(emoji_result)
        # Check if user's guess is correct
        if user_guess == secret_word:
            print("You won in " +  str(turn) + "/" + str(max_turns) + " turns!")
            return
        # Move on to next turn
        turn += 1
    # User doesn't guess the word in max_turns, print a message
    print("X/" + str(max_turns) + " - Sorry, try again tomorrow!")

    if __name__ == "__main__":
        main()