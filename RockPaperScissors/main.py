from Players.HumanPlayer import HumanPlayer
from RockPaperScissors.Players.PCPlayer import PCPlayer
from RockPaperScissors.logic.RockPaperScissorsGame import RockPaperScissorsGame
from RockPaperScissors.logic.WinnerHandler import WinnerHandler
from UI.ConsoleUI import ConsoleUI

console_UI = ConsoleUI()
human_player = HumanPlayer(console_UI)
pc_player = PCPlayer()

winner_handler = WinnerHandler(human_player, pc_player)
game = RockPaperScissorsGame(console_UI, winner_handler, 3)

game.play_game()

print("Hello, World!")