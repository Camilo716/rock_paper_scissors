from Players.IPlayer import IPlayer
from UI.IRockPaperScsUI import IRockPaperScsUI
import logic.Moves as Moves

class RockPaperScissorsGame():
    
    def __init__(self, UI:IRockPaperScsUI, human_player:IPlayer, pc_player:IPlayer, rounds:IPlayer):
        self.UI = UI
        self.human_player = human_player
        self.pc_player = pc_player

    def play_game(self):
        self.finishGame = False;

    def compare_moves():
        pass
        
        
            
    