from Players.IPlayer import IPlayer
from RockPaperScissors.Logic.Moves import Moves
from UI.IRockPaperScsUI import IRockPaperScsUI;

class HumanPlayer(IPlayer):
    def __init__(self, UI: IRockPaperScsUI):
        self.UI = UI

    def choose_move(self):
        valid_moves = list(move.value for move in Moves)

        while True:
            value_choosen_move = int(self.UI.read_player_move())

            if value_choosen_move not in valid_moves:
                self.UI.show_game_msj("Invalid Movement")
                continue
            
            self.name_choosen_move = Moves(int(value_choosen_move)).name
            return  self.name_choosen_move
            
            
             
            