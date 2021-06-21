from typing import Tuple

from .piece import Piece


class Quilt(object):
    def __init__(self, size):
        self.occupied_spaces = [[False for _ in range(size)] for _ in range(size)]
        self.total_button_gain = 0

    def is_position_occupied(self, position):
        # type: (Tuple[int, int]) -> bool
        x, y = position
        return self.occupied_spaces[y][x]

    def set_position_occupied(self, position):
        # type: (Tuple[int, int]) -> None
        x, y = position
        self.occupied_spaces[y][x] = True

    def can_piece_be_placed_at_position(self, piece, position, rotation):
        # type: (Piece, Tuple[int, int], int) -> bool
        if self.is_position_occupied(position):
            return False

        x, y = position
        for square_offset in piece.get_rotated_square_offsets(rotation):
            if self.is_position_occupied((x + square_offset[0], y + square_offset[1])):
                return False

        return True

    def add_piece_to_board(self, piece, position, rotation):
        # type: (Piece, Tuple[int, int], int) -> None
        self.set_position_occupied(position)

        x, y = position
        for square_offset in piece.get_rotated_square_offsets(rotation):
            self.set_position_occupied((x + square_offset[0], y + square_offset[1]))

        self.total_button_gain += piece.button_gain