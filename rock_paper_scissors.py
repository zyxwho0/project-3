import random


def get_computer_choice():
    """Return a random choice for the computer."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def get_user_choice():
    """Get and validate user's choice."""
    while True:
        user_input = input("Enter your choice (rock/paper/scissors) or 'quit' to exit: ").lower().strip()
        if user_input in ["rock", "paper", "scissors", "quit"]:
            return user_input
        print("Invalid choice! Please try again.")


def determine_winner(user_choice, computer_choice):
    """Determine the winner and return the result."""
    if user_choice == computer_choice:
        return "tie"
    
    winning_combinations = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    # Validate inputs to ensure a well-defined failure mode
    valid_choices = set(winning_combinations.keys())
    if user_choice not in valid_choices:
        raise ValueError(f"Invalid user_choice: {user_choice!r}. Expected one of: {sorted(valid_choices)}")
    if computer_choice not in valid_choices:
        raise ValueError(f"Invalid computer_choice: {computer_choice!r}. Expected one of: {sorted(valid_choices)}")
    
    if winning_combinations[user_choice] == computer_choice:
        return "user"
    return "computer"


def display_result(user_choice, computer_choice, winner):
    """Display the game result."""
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win! 🎉")
    else:
        print("Computer wins!")


def play_game():
    """Main game loop."""
    print("=" * 40)
    print("Welcome to Rock-Paper-Scissors!")
    print("=" * 40)
    
    user_score = 0
    computer_score = 0
    
    while True:
        user_choice = get_user_choice()
        
        if user_choice == "quit":
            break
        
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)
        
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        
        print(f"\nScore - You: {user_score} | Computer: {computer_score}")
        print("-" * 40)
    
    print("\n" + "=" * 40)
    print("Thanks for playing!")
    print(f"Final Score - You: {user_score} | Computer: {computer_score}")
    print("=" * 40)


if __name__ == "__main__":
    play_game()
