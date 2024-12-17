import random
import time

def computer_guesses(low, high):
    attempts = 0
    start_time = time.time()

    print(f"\nThink of a number between {low} and {high}, and I will guess it.")
    input("Press Enter when you have thought of the number")

    while True:
        attempts += 1
        guess = (low + high) // 2
        user_feedback = input(f"Is your number {guess}? (Enter 'high', 'low', or 'correct'): ").lower()

        if user_feedback == "low":
            low = guess + 1
        elif user_feedback == "high":
            high = guess - 1
        elif user_feedback == "correct":
            end_time = time.time()
            elapsed_time = round(end_time - start_time, 2)
            print(f"\nI guessed it! Your number is {guess}.")
            print(f"It took me {attempts} attempts and {elapsed_time} seconds.")
            break
        else:
            print("Invalid input. Please enter 'high', 'low', or 'correct'.")

def play_again():
    while True:
        response = input("\nDo you want to play again? (yes/no): ").lower()
        if response == "yes":
            return True
        elif response == "no":
            print("Thank you for playing")
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    while True:
        computer_guesses(1, 100)
        if not play_again():
            break