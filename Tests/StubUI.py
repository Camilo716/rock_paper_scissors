from UI.IRockPaperScsUI import IRockPaperScsUI


class ConsoleUI(IRockPaperScsUI):
    
    def read_player_move(self, prompt):
        return input(prompt)
    
    def show_game_msj (self, msj):
        return msj
