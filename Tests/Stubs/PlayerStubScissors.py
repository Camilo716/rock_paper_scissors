from Players.IPlayer import IPlayer
from logic.Moves import Moves

class PlayerStubScissors(IPlayer):
    def choose_move(self):
        return Moves.Scissors; 
