from RockPaperScissors.Players.IPlayer import IPlayer
from RockPaperScissors.logic.Moves import Moves 

class PlayerStubScissors(IPlayer):
    def choose_move(self):
        return Moves.Scissors; 
