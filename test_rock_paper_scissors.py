import pytest
from rock_paper_scissors import determine_winner


# --- determine_winner: tie cases ---

def test_determine_winner_rock_tie():
    assert determine_winner("rock", "rock") == "tie"


def test_determine_winner_paper_tie():
    assert determine_winner("paper", "paper") == "tie"


def test_determine_winner_scissors_tie():
    assert determine_winner("scissors", "scissors") == "tie"


# --- determine_winner: user wins ---

def test_determine_winner_rock_beats_scissors():
    assert determine_winner("rock", "scissors") == "user"


def test_determine_winner_paper_beats_rock():
    assert determine_winner("paper", "rock") == "user"


def test_determine_winner_scissors_beats_paper():
    assert determine_winner("scissors", "paper") == "user"


# --- determine_winner: computer wins ---

def test_determine_winner_scissors_loses_to_rock():
    assert determine_winner("scissors", "rock") == "computer"


def test_determine_winner_rock_loses_to_paper():
    assert determine_winner("rock", "paper") == "computer"


def test_determine_winner_paper_loses_to_scissors():
    assert determine_winner("paper", "scissors") == "computer"


# --- determine_winner: invalid inputs ---

def test_determine_winner_invalid_user_choice():
    with pytest.raises(ValueError, match="Invalid user_choice"):
        determine_winner("lizard", "rock")


def test_determine_winner_invalid_computer_choice():
    with pytest.raises(ValueError, match="Invalid computer_choice"):
        determine_winner("rock", "spock")
