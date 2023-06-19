from Players.IPlayer import IPlayer
from RockPaperScissors.logic.Moves import Moves
from UI.IRockPaperScsUI import IRockPaperScsUI;

class HumanPlayer(IPlayer):
    def __init__(self, UI: IRockPaperScsUI):
        self.UI = UI

    def choose_move(self):
        valid_moves = list(move.value for move in Moves)

        while True:
            self.choosen_move = self.UI.read_player_move()
            
            if self.choosen_move in valid_moves:
                self.UI.show_game_msj("Invalid Movement")
                continue
            
            self.choosen_move = Moves(self.choosen_move).name
            return  self.choosen_move
            
            
             
            