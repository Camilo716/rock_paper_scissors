from RockPaperScissors.Logic.Players import IPlayer
from RockPaperScissors.Logic.Moves import Moves

class WinnerHandler():
    
    def __init__(self, player1:IPlayer, player2:IPlayer):
        self.player1 = player1
        self.player2 = player2 


    def compare_moves(self):
        P1_move = self.player1.choose_move()
        P2_move = self.player2.choose_move()

        Player1WinCases = (
            (P1_move == Moves.Rock) and (P2_move == Moves.Scissors),
            (P1_move == Moves.Paper) and (P2_move == Moves.Rock),  
            (P1_move == Moves.Scissors) and (P2_move == Moves.Paper),
        ) 

        Player2WinCases = (
            (P2_move == Moves.Rock) and (P1_move == Moves.Scissors),
            (P2_move == Moves.Paper) and (P1_move == Moves.Rock),  
            (P2_move == Moves.Scissors) and (P1_move == Moves.Paper),
        )

        if self.player_wins(Player1WinCases):
            return self.player1

        if self.player_wins(Player2WinCases):
            return self.player2

    def player_wins(self, player_win_cases):
        for case in player_win_cases:
            if case:
                return True
        
        return False