import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a Tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        return "You Win"
    else:
        return "Computer Wins"

def play_game():
    choices = ["Rock", "Paper", "Scissors"]
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        player_choice = input("Choose Rock, Paper, or Scissors (or 'quit' to exit): ").capitalize()
        if player_choice == 'Quit':
            print("Thanks for playing! Goodbye.")
            break
        elif player_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(choices)
        result = determine_winner(player_choice, computer_choice)
        print(f"You chose: {player_choice}\nComputer chose: {computer_choice}\n{result}\n")

def main():
    play_game()

if __name__ == "__main__":
    main()
