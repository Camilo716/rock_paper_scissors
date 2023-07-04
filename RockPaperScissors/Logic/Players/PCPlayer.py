import random

from Players.IPlayer import IPlayer
from RockPaperScissors.Logic.Moves import Moves

class PCPlayer(IPlayer):
    def __init__(self):
        pass

    def choose_move(self):
        moves = list(Moves)
        self.choosen_move = random.choice(moves)
        
        self.choosen_move = Moves(self.choosen_move).name
        return self.choosen_move