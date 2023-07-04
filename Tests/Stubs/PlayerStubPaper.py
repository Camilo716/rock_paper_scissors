from RockPaperScissors.Logic.Players.IPlayer import IPlayer
from RockPaperScissors.Logic.Moves import Moves


class PlayerStubPaper(IPlayer):    
    def choose_move(self):
        return Moves.Paper; 