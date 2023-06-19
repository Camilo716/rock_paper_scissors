import unittest
from RockPaperScissors.logic.Moves import Moves
from RockPaperScissors.logic.RockPaperScissorsGame import RockPaperScissorsGame

from Tests.Stubs.PlayerStubScissors import PlayerStubScissors
from Tests.Stubs.PlayerStubPaper import PlayerStubPaper
from Tests.Stubs.PlayerStubRock import PlayerStubRock

class GameTest(unittest.TestCase):

    def test_compare_moves(self): 

        WinnerGameCases = [
            (PlayerStubPaper(), PlayerStubRock(), PlayerStubPaper()),
            (PlayerStubPaper(), PlayerStubScissors(), PlayerStubScissors()),
            (PlayerStubScissors(), PlayerStubRock(), PlayerStubRock()),
        ]

        for player1, player2, winner_expected in WinnerGameCases:
            game = RockPaperScissorsGame(player1, player2, 1)
            
            winner = game.compare_moves(player1, player2)

            self.assertEqual(winner, winner_expected)     

if __name__ == '__main__':
    unittest.main()