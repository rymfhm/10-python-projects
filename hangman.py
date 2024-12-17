import random
import string

def display_word_progress(word, used_letters):
    return ' '.join([letter if letter in used_letters else '-' for letter in word])

def get_valid_word(word_list):
    word = random.choice(word_list)
    while '-' in word or ' ' in word:
        word = random.choice(word_list)
    return word.upper()

def hangman(words):
    print("Welcome to the Hangman Game")
    print("Guess the correct letters to save your lives.\n")

    word = get_valid_word(words)
    alphabet = set(string.ascii_uppercase)
    word_letters = set(word)
    used_letters = set()
    lives = 7

    hangman_stages = [
        "\n   +---+\n       |\n       |\n       |\n      ===\n",
        "\n   +---+\n   O   |\n       |\n       |\n      ===\n",
        "\n   +---+\n   O   |\n   |   |\n       |\n      ===\n",
        "\n   +---+\n   O   |\n  /|   |\n       |\n      ===\n",
        "\n   +---+\n   O   |\n  /|\  |\n       |\n      ===\n",
        "\n   +---+\n   O   |\n  /|\  |\n  /    |\n      ===\n",
        "\n   +---+\n   O   |\n  /|\  |\n  / \  |\n      ===\n"
    ]

    while len(word_letters) > 0 and lives > 0:
        print(f"Lives remaining: {lives}")
        print(hangman_stages[7 - lives])
        print(f"Used letters: {' '.join(used_letters)}")
        print("Current word: ", display_word_progress(word, used_letters))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print(f"Incorrect guess. {user_letter} is not in the word.\n")
        elif user_letter in used_letters:
            print("You already guessed that letter. Try again.\n")
        else:
            print("Invalid input. Please enter a valid letter.\n")

    if lives == 0:
        print(hangman_stages[6])
        print(f"You lost The word was {word}. Better luck next time!")
    else:
        print(f"Congratulations You guessed the word correctly: {word}!")

def main():
    words = ["python", "development", "hangman", "programming", "advanced", "algorithm", "challenge"]
    hangman(words)

if __name__ == "__main__":
    main()