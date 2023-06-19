from Players.IPlayer import IPlayer
from logic.Moves import Moves

class PlayerStubRock(IPlayer):
    def choose_move(self):
        return Moves.Rock; 