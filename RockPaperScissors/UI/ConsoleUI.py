from UI.IRockPaperScsUI import IRockPaperScsUI


class ConsoleUI(IRockPaperScsUI):
    
    def read_player_move(self):
        return input(
            """
                Write number of your next move
                1. Rock
                3. Paper
                4. Scissors
            """ 
        )
    
    def show_game_msj (self, msj):
        print(msj)



    