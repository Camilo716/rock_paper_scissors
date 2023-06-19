from Players.IPlayer import IPlayer
from logic.Moves import Moves

class PlayerStubPaper(IPlayer):
    def choose_move(self):
        return Moves.Paper; 