from Players.IPlayer import IPlayer
from RockPaperScissors.logic.Moves import Moves
from UI.IRockPaperScsUI import IRockPaperScsUI;

class HumanPlayer(IPlayer):
    def __init__(self, UI: IRockPaperScsUI):
        self.UI = UI

    def choose_move(self):
        valid_moves = list(move.value for move in Moves)

        while True:
            choosen_move = self.UI.read_player_move()
            
            if choosen_move in valid_moves:
                self.UI.show_game_msj("Invalid Movement")
                continue

            return choosen_move
            
            
             
            