import unittest
from RockPaperScissors.logic.WinnerHandler import WinnerHandler

from Tests.Stubs.PlayerStubPaper import PlayerStubPaper
from Tests.Stubs.PlayerStubRock import PlayerStubRock
from Tests.Stubs.PlayerStubScissors import PlayerStubScissors

class test_winner_handler(unittest.TestCase):

    def test_find_winner(self): 
        stub_paper = PlayerStubPaper("StubPaper")
        stub_rock = PlayerStubRock("StubRock")
        stub_scissors = PlayerStubScissors("StubScissors")
         
        WinnerGameCases = [ 
            (stub_paper, stub_rock, stub_paper),
            (stub_paper, stub_scissors, stub_scissors),
            (stub_scissors, stub_rock, stub_rock),
        ]

        for player1, player2, winner_expected in WinnerGameCases:
            winner_handler = WinnerHandler(player1, player2)
            
            winner = winner_handler.compare_moves()
            
            self.assertEqual(winner, winner_expected)     

if __name__ == '__main__':
    unittest.main()