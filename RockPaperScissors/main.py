from RockPaperScissors.Logic.Players.HumanPlayer import HumanPlayer
from RockPaperScissors.Logic.Players.PCPlayer import PCPlayer
from RockPaperScissors.Logic.RockPaperScissorsGame import RockPaperScissorsGame
from RockPaperScissors.Logic.WinnerHandler import WinnerHandler
from UI.ConsoleUI import ConsoleUI

console_UI = ConsoleUI()
human_player = HumanPlayer("Human", console_UI)
pc_player = PCPlayer("Pc")

winner_handler = WinnerHandler(human_player, pc_player)
game = RockPaperScissorsGame(console_UI, winner_handler, 3)

game.play_game()