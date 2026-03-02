import tkinter as tk
from tkinter import messagebox
from rock_paper_scissors import get_computer_choice, determine_winner


class RockPaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("500x600")
        self.root.configure(bg="#2c3e50")
        
        self.user_score = 0
        self.computer_score = 0
        
        # Title
        title = tk.Label(
            root,
            text="Rock Paper Scissors",
            font=("Arial", 24, "bold"),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        title.pack(pady=20)
        
        # Score display
        self.score_label = tk.Label(
            root,
            text=f"You: {self.user_score} | Computer: {self.computer_score}",
            font=("Arial", 14),
            bg="#2c3e50",
            fg="#3498db"
        )
        self.score_label.pack(pady=10)
        
        # Choices display
        self.choices_frame = tk.Frame(root, bg="#2c3e50")
        self.choices_frame.pack(pady=20)
        
        self.user_choice_label = tk.Label(
            self.choices_frame,
            text="Your choice: -",
            font=("Arial", 12),
            bg="#2c3e50",
            fg="#2ecc71"
        )
        self.user_choice_label.pack()
        
        self.computer_choice_label = tk.Label(
            self.choices_frame,
            text="Computer's choice: -",
            font=("Arial", 12),
            bg="#2c3e50",
            fg="#e74c3c"
        )
        self.computer_choice_label.pack()
        
        # Result display
        self.result_label = tk.Label(
            root,
            text="Make your choice!",
            font=("Arial", 14, "bold"),
            bg="#2c3e50",
            fg="#f39c12"
        )
        self.result_label.pack(pady=15)
        
        # Buttons
        button_frame = tk.Frame(root, bg="#2c3e50")
        button_frame.pack(pady=20)
        
        rock_btn = tk.Button(
            button_frame,
            text="🪨 Rock",
            font=("Arial", 12),
            width=10,
            bg="#34495e",
            fg="#ecf0f1",
            command=lambda: self.play("rock")
        )
        rock_btn.grid(row=0, column=0, padx=5)
        
        paper_btn = tk.Button(
            button_frame,
            text="📄 Paper",
            font=("Arial", 12),
            width=10,
            bg="#34495e",
            fg="#ecf0f1",
            command=lambda: self.play("paper")
        )
        paper_btn.grid(row=0, column=1, padx=5)
        
        scissors_btn = tk.Button(
            button_frame,
            text="✂️ Scissors",
            font=("Arial", 12),
            width=10,
            bg="#34495e",
            fg="#ecf0f1",
            command=lambda: self.play("scissors")
        )
        scissors_btn.grid(row=0, column=2, padx=5)
        
        # Reset button
        reset_btn = tk.Button(
            root,
            text="Reset Score",
            font=("Arial", 10),
            bg="#e74c3c",
            fg="#ecf0f1",
            command=self.reset_score
        )
        reset_btn.pack(pady=10)
    
    def play(self, user_choice):
        """Play a round of the game."""
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        
        # Update choice labels
        self.user_choice_label.config(text=f"Your choice: {user_choice}")
        self.computer_choice_label.config(text=f"Computer's choice: {computer_choice}")
        
        # Update score and result
        if winner == "tie":
            result_text = "It's a Tie! 🤝"
            self.result_label.config(text=result_text, fg="#f39c12")
        elif winner == "user":
            self.user_score += 1
            result_text = "You Win! 🎉"
            self.result_label.config(text=result_text, fg="#2ecc71")
        else:  # computer wins
            self.computer_score += 1
            result_text = "Computer Wins! 🤖"
            self.result_label.config(text=result_text, fg="#e74c3c")
        
        # Update score label
        self.score_label.config(
            text=f"You: {self.user_score} | Computer: {self.computer_score}"
        )
    
    def reset_score(self):
        """Reset the score."""
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(
            text=f"You: {self.user_score} | Computer: {self.computer_score}"
        )
        self.user_choice_label.config(text="Your choice: -")
        self.computer_choice_label.config(text="Computer's choice: -")
        self.result_label.config(text="Make your choice!", fg="#f39c12")


if __name__ == "__main__":
    root = tk.Tk()
    gui = RockPaperScissorsGUI(root)
    root.mainloop()
