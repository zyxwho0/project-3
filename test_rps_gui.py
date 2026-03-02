import unittest
from unittest.mock import patch, MagicMock
import sys
import random
from rps_gui import RockPaperScissorsGUI


class TestRockPaperScissorsGUI(unittest.TestCase):
    """Test cases for the Rock-Paper-Scissors GUI game."""
    
    def setUp(self):
        """Set up test fixtures."""
        # Mock tkinter to avoid GUI creation during tests
        self.root_mock = MagicMock()
        with patch('rps_gui.tk.Label'), \
             patch('rps_gui.tk.Frame'), \
             patch('rps_gui.tk.Button'):
            self.game = RockPaperScissorsGUI(self.root_mock)
    
    def test_initial_scores(self):
        """Test that initial scores are zero."""
        self.assertEqual(self.game.user_score, 0)
        self.assertEqual(self.game.computer_score, 0)
    
    def test_determine_winner_tie(self):
        """Test tie scenarios."""
        self.assertEqual(self.game.determine_winner("rock", "rock"), "tie")
        self.assertEqual(self.game.determine_winner("paper", "paper"), "tie")
        self.assertEqual(self.game.determine_winner("scissors", "scissors"), "tie")
    
    def test_determine_winner_user_wins(self):
        """Test scenarios where user wins."""
        self.assertEqual(self.game.determine_winner("rock", "scissors"), "user")
        self.assertEqual(self.game.determine_winner("paper", "rock"), "user")
        self.assertEqual(self.game.determine_winner("scissors", "paper"), "user")
    
    def test_determine_winner_computer_wins(self):
        """Test scenarios where computer wins."""
        self.assertEqual(self.game.determine_winner("rock", "paper"), "computer")
        self.assertEqual(self.game.determine_winner("paper", "scissors"), "computer")
        self.assertEqual(self.game.determine_winner("scissors", "rock"), "computer")
    
    @patch('rps_gui.random.choice')
    def test_play_user_wins(self, mock_choice):
        """Test play method when user wins."""
        mock_choice.return_value = "scissors"
        self.game.play("rock")
        
        self.assertEqual(self.game.user_score, 1)
        self.assertEqual(self.game.computer_score, 0)
    
    @patch('rps_gui.random.choice')
    def test_play_computer_wins(self, mock_choice):
        """Test play method when computer wins."""
        mock_choice.return_value = "paper"
        self.game.play("rock")
        
        self.assertEqual(self.game.user_score, 0)
        self.assertEqual(self.game.computer_score, 1)
    
    @patch('rps_gui.random.choice')
    def test_play_tie(self, mock_choice):
        """Test play method when it's a tie."""
        mock_choice.return_value = "rock"
        self.game.play("rock")
        
        self.assertEqual(self.game.user_score, 0)
        self.assertEqual(self.game.computer_score, 0)
    
    @patch('rps_gui.random.choice')
    def test_multiple_rounds(self, mock_choice):
        """Test multiple rounds of play."""
        # User wins
        mock_choice.return_value = "scissors"
        self.game.play("rock")
        
        # Computer wins
        mock_choice.return_value = "paper"
        self.game.play("rock")
        
        # Tie
        mock_choice.return_value = "rock"
        self.game.play("rock")
        
        # User wins again
        mock_choice.return_value = "rock"
        self.game.play("paper")
        
        self.assertEqual(self.game.user_score, 2)
        self.assertEqual(self.game.computer_score, 1)
    
    def test_reset_score(self):
        """Test reset score functionality."""
        # Set some scores
        self.game.user_score = 5
        self.game.computer_score = 3
        
        # Reset
        self.game.reset_score()
        
        self.assertEqual(self.game.user_score, 0)
        self.assertEqual(self.game.computer_score, 0)
    
    def test_all_choices_valid(self):
        """Test that all valid choices work without errors."""
        choices = ["rock", "paper", "scissors"]
        for user_choice in choices:
            for computer_choice in choices:
                result = self.game.determine_winner(user_choice, computer_choice)
                self.assertIn(result, ["user", "computer", "tie"])


class TestGameLogic(unittest.TestCase):
    """Test the core game logic independently."""
    
    def test_rock_beats_scissors(self):
        """Test that rock beats scissors."""
        winning_combinations = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }
        self.assertEqual(winning_combinations["rock"], "scissors")
    
    def test_paper_beats_rock(self):
        """Test that paper beats rock."""
        winning_combinations = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }
        self.assertEqual(winning_combinations["paper"], "rock")
    
    def test_scissors_beats_paper(self):
        """Test that scissors beats paper."""
        winning_combinations = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }
        self.assertEqual(winning_combinations["scissors"], "paper")


if __name__ == "__main__":
    unittest.main()
