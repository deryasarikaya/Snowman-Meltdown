import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Returns a random word from the WORDS list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current snowman stage and the progress of the guessed word."""

    print("-" * 30)
    print(STAGES[mistakes])

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print()
    print("-" * 30)


def get_valid_guess():
    """Gets a valid single letter guess from the user."""
    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("Please enter only one letter.")
        elif not guess.isalpha():
            print("Please enter a letter from A to Z.")
        else:
            return guess


def start_game():
    """Handles replay option."""
    while True:
        play_game()

        choice = input("Play again? (y/n): ").lower()

        if choice != "y":
            print("Goodbye!")
            break


def play_game():
    """Runs the main game loop until the player wins or loses."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = get_valid_guess()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in secret_word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            guessed_letters.append(guess)
            mistakes += 1
            print("Wrong guess!")

        all_letters_guessed = True

        for letter in secret_word:
            if letter not in guessed_letters:
                all_letters_guessed = False

        if all_letters_guessed:
            display_game_state(mistakes, secret_word, guessed_letters)
            print("You saved the snowman!")
            return

    display_game_state(mistakes, secret_word, guessed_letters)
    print("The snowman melted!")