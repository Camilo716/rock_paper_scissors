from RockPaperScissors.Logic.Players.IPlayer import IPlayer
from RockPaperScissors.Logic.Moves import Moves 

class PlayerStubScissors(IPlayer):
    def choose_move(self):
        return Moves.Scissors; 
