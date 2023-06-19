import random

from Players.IPlayer import IPlayer
from RockPaperScissors.logic.Moves import Moves
from UI.IRockPaperScsUI import IRockPaperScsUI;

class PCPlayer(IPlayer):
    def __init__(self):
        pass

    def choose_move(self):
        moves = list(Moves)
        random_move = random.choice(moves)
        
        return random_move