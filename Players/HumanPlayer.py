from Players.IPlayer import IPlayer
from UI.IRockPaperScsUI import IRockPaperScsUI;

class HumanPlayer(IPlayer):
    def __init__(self, UI: IRockPaperScsUI):
        self.UI = UI

    def choose_move(self):
        while True:
            self.UI.read_player_move()
            
             
            