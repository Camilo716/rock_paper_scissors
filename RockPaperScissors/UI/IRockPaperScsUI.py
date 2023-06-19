from abc import ABC, abstractmethod


class IRockPaperScsUI(ABC):
    @abstractmethod
    def read_player_move(self):
        pass

    @abstractmethod
    def show_game_msj(self, msj):
        pass
