from Players.IPlayer import IPlayer
from RockPaperScissors.logic.Moves import Moves
from UI.IRockPaperScsUI import IRockPaperScsUI

class WinnerHandler():
    
    def __init__(self, player1:IPlayer, player2:IPlayer):
        self.player1 = player1
        self.player2 = player2 

    def compare_moves(self):
        P1_move = self.player1.choose_move()
        P2_move = self.player2.choose_move()

        Player1WinCases = (
            (P1_move == Moves.Rock) & (P2_move == Moves.Scissors),
            (P1_move == Moves.Paper) & (P2_move == Moves.Rock),  
            (P1_move == Moves.Scissors) & (P2_move == Moves.Paper),
        ) 

        Player2WinCases = (
            (P2_move == Moves.Rock) & (P1_move == Moves.Scissors),
            (P2_move == Moves.Paper) & (P1_move == Moves.Rock),  
            (P2_move == Moves.Scissors) & (P1_move == Moves.Paper),
        )

        if self.player1_wins(Player1WinCases):
            return self.player1

        if self.player2_wins(Player2WinCases):
            return self.player1
    
    def player1_wins(self, P1_win_cases):
        for case in P1_win_cases:
            return case == True
        
        return False
    
    def player2_wins(self, P2_win_cases):
        for case in P2_win_cases:
            return case == True
        
        return False