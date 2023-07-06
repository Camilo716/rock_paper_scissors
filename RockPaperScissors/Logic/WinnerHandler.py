from RockPaperScissors.Logic.Players.IPlayer import IPlayer
from RockPaperScissors.Logic.Moves import Moves

class WinnerHandler():
    
    def __init__(self, player1:IPlayer, player2:IPlayer):
        self.player1 = player1
        self.player2 = player2 

    def compare_moves(self):
        P1_move = self.player1.choose_move()
        P2_move = self.player2.choose_move()

        # {case : winner}
        win_cases = {
            (Moves.Rock, Moves.Scissors): self.player1,
            (Moves.Paper, Moves.Rock): self.player1,
            (Moves.Scissors, Moves.Paper): self.player1,

            (Moves.Scissors, Moves.Rock): self.player2,
            (Moves.Rock, Moves.Paper): self.player2,
            (Moves.Paper, Moves.Scissors): self.player2,
        }

        winner = win_cases.get((P1_move, P2_move))
        return winner