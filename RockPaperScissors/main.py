from Players.HumanPlayer import HumanPlayer
from RockPaperScissors.logic.RockPaperScissorsGame import RockPaperScissorsGame
from RockPaperScissors.logic.WinnerHandler import WinnerHandler
from UI.ConsoleUI import ConsoleUI

console_UI = ConsoleUI()
human_player = HumanPlayer()
pc_player = PCPlayer()

winner_handler = WinnerHandler(human_player, pc_player)
game = RockPaperScissorsGame(winner_handler, 3)

game.play_game()