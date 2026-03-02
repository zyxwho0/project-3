import pytest
from rock_paper_scissors import (
    get_computer_choice,
    determine_winner,
)


# --- get_computer_choice ---

def test_get_computer_choice_returns_valid_choice():
    """Test that computer choice is one of the valid options."""
    valid_choices = {"rock", "paper", "scissors"}
    choice = get_computer_choice()
    assert choice in valid_choices


def test_get_computer_choice_returns_string():
    """Test that computer choice returns a string."""
    choice = get_computer_choice()
    assert isinstance(choice, str)


# --- determine_winner ---

def test_determine_winner_tie():
    """Test tie scenarios."""
    assert determine_winner("rock", "rock") == "tie"
    assert determine_winner("paper", "paper") == "tie"
    assert determine_winner("scissors", "scissors") == "tie"


def test_determine_winner_user_wins():
    """Test user winning scenarios."""
    assert determine_winner("rock", "scissors") == "user"
    assert determine_winner("paper", "rock") == "user"
    assert determine_winner("scissors", "paper") == "user"


def test_determine_winner_computer_wins():
    """Test computer winning scenarios."""
    assert determine_winner("scissors", "rock") == "computer"
    assert determine_winner("rock", "paper") == "computer"
    assert determine_winner("paper", "scissors") == "computer"


def test_determine_winner_invalid_user_choice():
    """Test that invalid user choice raises ValueError."""
    with pytest.raises(ValueError):
        determine_winner("invalid", "rock")


def test_determine_winner_invalid_computer_choice():
    """Test that invalid computer choice raises ValueError."""
    with pytest.raises(ValueError):
        determine_winner("rock", "invalid")


def test_determine_winner_both_invalid():
    """Test that both invalid choices raise ValueError."""
    with pytest.raises(ValueError):
        determine_winner("invalid1", "invalid2")
