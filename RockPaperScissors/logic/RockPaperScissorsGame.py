from ..UI.IRockPaperScsUI import IRockPaperScsUI

class RockPaperScissorsGame():
    
    def __init__(self, UI:IRockPaperScsUI, winner_handler, rounds):
        self.UI = UI
        self.winner_handler = winner_handler
        self.rounds = rounds

    def play_game(self):
        self.UI.show_game_msj("Welcome to rock paper ScissorsGame")
        for _ in range(self.rounds):
            winner = self.winner_handler.compare_moves()


        
        
            
    