from RockPaperScissors.Players.IPlayer import IPlayer
from RockPaperScissors.logic.Moves import Moves


class PlayerStubPaper(IPlayer):
    def choose_move(self):
        return Moves.Paper; 