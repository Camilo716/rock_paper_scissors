from Players.IPlayer import IPlayer
import UI.IRockPaperScsUI;

class HumanPlayer(IPlayer):
    def __init__(self, UI):
        self.UI = UI

    def choose_move(self):
        while True:
            UI.read_player_move()
            
             
            