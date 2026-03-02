import tkinter as tk
from tkinter import ttk
import random


class RockPaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        
        self.user_score = 0
        self.computer_score = 0
        
        self.setup_ui()
    
    def setup_ui(self):
        """Set up the user interface."""
        # Title
        title_label = tk.Label(
            self.root,
            text="Rock Paper Scissors",
            font=("Arial", 24, "bold"),
            fg="#2c3e50",
            pady=20
        )
        title_label.pack()
        
        # Score frame
        score_frame = tk.Frame(self.root, bg="#ecf0f1", pady=15)
        score_frame.pack(fill="x", padx=20, pady=10)
        
        self.user_score_label = tk.Label(
            score_frame,
            text=f"Your Score: {self.user_score}",
            font=("Arial", 16),
            bg="#ecf0f1"
        )
        self.user_score_label.pack(side="left", padx=40)
        
        self.computer_score_label = tk.Label(
            score_frame,
            text=f"Computer Score: {self.computer_score}",
            font=("Arial", 16),
            bg="#ecf0f1"
        )
        self.computer_score_label.pack(side="right", padx=40)
        
        # Choices display frame
        choices_frame = tk.Frame(self.root, pady=20)
        choices_frame.pack()
        
        # User choice
        user_choice_frame = tk.Frame(choices_frame)
        user_choice_frame.pack(side="left", padx=30)
        
        tk.Label(
            user_choice_frame,
            text="Your Choice",
            font=("Arial", 14, "bold"),
            fg="#3498db"
        ).pack()
        
        self.user_choice_label = tk.Label(
            user_choice_frame,
            text="?",
            font=("Arial", 60),
            width=3,
            height=2
        )
        self.user_choice_label.pack()
        
        # VS label
        tk.Label(
            choices_frame,
            text="VS",
            font=("Arial", 20, "bold"),
            fg="#e74c3c"
        ).pack(side="left", padx=20)
        
        # Computer choice
        computer_choice_frame = tk.Frame(choices_frame)
        computer_choice_frame.pack(side="left", padx=30)
        
        tk.Label(
            computer_choice_frame,
            text="Computer Choice",
            font=("Arial", 14, "bold"),
            fg="#e74c3c"
        ).pack()
        
        self.computer_choice_label = tk.Label(
            computer_choice_frame,
            text="?",
            font=("Arial", 60),
            width=3,
            height=2
        )
        self.computer_choice_label.pack()
        
        # Result label
        self.result_label = tk.Label(
            self.root,
            text="Choose your weapon!",
            font=("Arial", 18, "bold"),
            fg="#27ae60",
            pady=20
        )
        self.result_label.pack()
        
        # Buttons frame
        buttons_frame = tk.Frame(self.root, pady=20)
        buttons_frame.pack()
        
        # Rock button
        rock_btn = tk.Button(
            buttons_frame,
            text="ROCK",
            font=("Arial", 14, "bold"),
            width=10,
            height=3,
            bg="#95a5a6",
            fg="white",
            cursor="hand2",
            command=lambda: self.play("rock")
        )
        rock_btn.pack(side="left", padx=10)
        
        # Paper button
        paper_btn = tk.Button(
            buttons_frame,
            text="PAPER",
            font=("Arial", 14, "bold"),
            width=10,
            height=3,
            bg="#3498db",
            fg="white",
            cursor="hand2",
            command=lambda: self.play("paper")
        )
        paper_btn.pack(side="left", padx=10)
        
        # Scissors button
        scissors_btn = tk.Button(
            buttons_frame,
            text="SCISSORS",
            font=("Arial", 14, "bold"),
            width=10,
            height=3,
            bg="#e74c3c",
            fg="white",
            cursor="hand2",
            command=lambda: self.play("scissors")
        )
        scissors_btn.pack(side="left", padx=10)
        
        # Reset button
        reset_btn = tk.Button(
            self.root,
            text="Reset Score",
            font=("Arial", 12),
            bg="#f39c12",
            fg="white",
            cursor="hand2",
            width=15,
            command=self.reset_score
        )
        reset_btn.pack(pady=20)
    
    def play(self, user_choice):
        """Play a round of the game."""
        computer_choice = random.choice(["rock", "paper", "scissors"])
        
        # Update choice displays
        self.user_choice_label.config(text=user_choice.upper())
        self.computer_choice_label.config(text=computer_choice.upper())
        
        # Determine winner
        winner = self.determine_winner(user_choice, computer_choice)
        
        # Update scores
        if winner == "user":
            self.user_score += 1
            self.result_label.config(text="You Win!", fg="#27ae60")
        elif winner == "computer":
            self.computer_score += 1
            self.result_label.config(text="Computer Wins!", fg="#e74c3c")
        else:
            self.result_label.config(text="It's a Tie!", fg="#f39c12")
        
        # Update score labels
        self.user_score_label.config(text=f"Your Score: {self.user_score}")
        self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")
    
    def determine_winner(self, user_choice, computer_choice):
        """Determine the winner of the round."""
        if user_choice == computer_choice:
            return "tie"
        
        winning_combinations = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }
        
        if winning_combinations[user_choice] == computer_choice:
            return "user"
        return "computer"
    
    def reset_score(self):
        """Reset the game score."""
        self.user_score = 0
        self.computer_score = 0
        self.user_score_label.config(text=f"Your Score: {self.user_score}")
        self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")
        self.user_choice_label.config(text="?")
        self.computer_choice_label.config(text="?")
        self.result_label.config(text="Choose your weapon!", fg="#27ae60")


if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGUI(root)
    root.mainloop()
