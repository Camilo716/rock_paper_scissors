from abc import ABC, abstractmethod


class IPlayer(ABC):
    def __init__(self, name):
        self.name = name
        self.score = 0

    @abstractmethod
    def choose_move(self):
        pass 