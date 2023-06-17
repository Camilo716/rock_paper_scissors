from Players.HumanPlayer import HumanPlayer
from UI.ConsoleUI import ConsoleUI

consoleUI = ConsoleUI()
humanPlayer = HumanPlayer(consoleUI)

ConsoleUI.read_player_move(
    """
    Write number of your next move
    1. Rock
    3. Paper
    4. Scissors
    """
);