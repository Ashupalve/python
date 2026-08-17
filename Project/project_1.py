
# Project 1 : Snake Water Gun Game

import random
# Choices available
CHOICES = ["snake", "water", "gun"]
def get_computer_choice():
    """Return computer's random choice."""
    return random.choice(CHOICES)
def get_user_choice():
    """Ask user for their choice and validate input."""
    while True:
        user_input = input("Enter your choice (snake/s, water/w, gun/g) or 'q' to quit: ").strip().lower()
        if user_input == 'q':
            return None
        if user_input in ("snake", "s"):
            return "snake"
        if user_input in ("water", "w"):
            return "water"
        if user_input in ("gun", "g"):
            return "gun"
        print("Invalid input. Try again.")
def decide_winner(user, computer):
    """Decide the winner based on game rules."""
    if user == computer:
        return "tie"
    elif (user == "snake" and computer == "water") or \
         (user == "water" and computer == "gun") or \
         (user == "gun" and computer == "snake"):
        return "user"
    else:
        return "computer"
def play_round():
    user_choice = get_user_choice()
    if user_choice is None:
        return None  # User chose to quit
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice} | Computer chose: {computer_choice}")
    result = decide_winner(user_choice, computer_choice)
    if result == "tie":
        print("It's a tie!\n")
    elif result == "user":
        print("You win this round! 🎉\n")
    else:
        print("Computer wins this round. 😅\n")
    return result
def play_game():
    print("Welcome to Snake-Water-Gun Game!")
    print("Rules: snake > water, water > gun, gun > snake\n")
    while True:
        result = play_round()
        if result is None:
            print("Thanks for playing! Goodbye.")
            break
# Start the game
if __name__ == "__main__":
    play_game()