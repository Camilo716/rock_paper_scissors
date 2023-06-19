from RockPaperScissors.Players.IPlayer import IPlayer
from RockPaperScissors.logic.Moves import Moves


class PlayerStubRock(IPlayer):
    def choose_move(self):
        return Moves.Rock; 