from typing import List


class Board(object):
    def __init__(self, squares):
        # type: (List[BoardSquare]) -> None
        self.squares = squares


class BoardSquare(object):
    def handle_move(self, player):
        pass


class ButtonSquare(BoardSquare):
    def handle_move(self, player):
        player.collect_buttons()
