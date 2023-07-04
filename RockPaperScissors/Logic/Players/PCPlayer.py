import random

from RockPaperScissors.Logic.Moves import Moves
from RockPaperScissors.Logic.Players.IPlayer import IPlayer

class PCPlayer(IPlayer):
    def __init__(self, name):
        super().__init__(name)


    def choose_move(self):
        moves = list(Moves)
        self.choosen_move = random.choice(moves)
        
        self.choosen_move = Moves(self.choosen_move)
        return self.choosen_move