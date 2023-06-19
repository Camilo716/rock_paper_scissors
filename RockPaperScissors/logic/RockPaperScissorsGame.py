from Players.IPlayer import IPlayer
from UI.IRockPaperScsUI import IRockPaperScsUI
import logic.Moves as Moves

class RockPaperScissorsGame():
    
    def __init__(self, UI:IRockPaperScsUI, winner_handler, rounds:IPlayer):
        self.UI = UI
        self.winner_handler = winner_handler

    def play_game(self):
        self.finishGame = False;
        
        
            
    