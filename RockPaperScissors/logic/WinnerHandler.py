from RockPaperScissors.Players import IPlayer
from RockPaperScissors.logic.Moves import Moves

class WinnerHandler():
    
    def __init__(self, player1:IPlayer, player2:IPlayer):
        self.player1 = player1
        self.player2 = player2 

    def compare_moves(self):
        P1_move = self.player1.choose_move()
        P2_move = self.player2.choose_move()

        Player1WinCases = (
            (P1_move == Moves.Rock.name) & (P2_move == Moves.Scissors.name),
            (P1_move == Moves.Paper.name) & (P2_move == Moves.Rock.name),  
            (P1_move == Moves.Scissors.name) & (P2_move == Moves.Paper.name),
        ) 

        Player2WinCases = (
            (P2_move == Moves.Rock.name) & (P1_move == Moves.Scissors.name),
            (P2_move == Moves.Paper.name) & (P1_move == Moves.Rock.name),  
            (P2_move == Moves.Scissors.name) & (P1_move == Moves.Paper.name),
        )

        if self.player1_wins(Player1WinCases):
            return self.player1

        if self.player2_wins(Player2WinCases):
            return self.player2
    
    def player1_wins(self, P1_win_cases):
        for case in P1_win_cases:
            if case:
                return True
        
        return False
    
    def player2_wins(self, P2_win_cases):
        for case in P2_win_cases:
            return case == True
        
        return False