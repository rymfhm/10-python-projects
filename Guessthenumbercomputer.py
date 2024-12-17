import random
import time

def get_valid_input(prompt, low, high):
    while True:
        try:
            value = int(input(prompt))
            if low <= value <= high:
                return value
            else:
                print(f"Please enter a number between {low} and {high}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def display_welcome_message():
    print("\n" + "="*40)
    print("This the number guessing game. With a Time Limit")
    print("="*40)
    print("\nGuess the number?")

def set_difficulty():
    print("\nSelect a difficulty level:")
    print("1. Easy (Range: 1 to 10)")
    print("2. Medium (Range: 1 to 50)")
    print("3. Hard (Range: 1 to 100)")
    print("4. Impossible (Range: 1 to 1,000)")

    difficulty = get_valid_input("Enter the difficulty level (1-4): ", 1, 4)
    ranges = {1: 10, 2: 50, 3: 100, 4: 1000}
    return ranges[difficulty]

def guess_the_number(range_limit):
    random_number = random.randint(1, range_limit)
    attempts = 0
    start_time = time.time()

    print(f"\n Guess the number between 1 and {range_limit}.")

    while True:
        attempts += 1
        guess = get_valid_input(f"Attempt {attempts}: Guess a number: ", 1, range_limit)

        if guess < random_number:
            print("Got a bit too down.")
        elif guess > random_number:
            print("Got a bit too high")
        else:
            end_time = time.time()
            elapsed_time = round(end_time - start_time, 2)
            print(f"\nCorrect! The number was {random_number}.")
            print(f"You guessed it in {attempts} attempts and {elapsed_time} seconds.")
            break

def play_again():
    while True:
        response = input("\nDo you want to play again? (yes): ").lower()
        if response == "yes":
            return True
        elif response == "no":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    display_welcome_message()
    while True:
        range_limit = set_difficulty()
        guess_the_number(range_limit)
        if not play_again():
            break