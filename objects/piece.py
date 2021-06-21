from typing import List, Tuple

class Piece(object):
    def __init__(self, square_offsets, button_cost, time_cost, button_gain):
        # type: (List[Tuple[int, int]], int, int, int) -> None
        self.square_offsets = square_offsets
        self.button_cost = button_cost
        self.time_cost = time_cost
        self.button_gain = button_gain

    def get_rotated_square_offsets(self, rotation):
        # type: (int) -> List[Tuple[int, int]]
        rotated_offsets = []
        for square_offset in self.square_offsets:
            offset_x, offset_y = square_offset
            if rotation == 90:
                rotated_offsets.append((offset_y, -offset_x))
            elif rotation == 180:
                rotated_offsets.append((-offset_x, -offset_y))
            else:
                assert rotation == 270, f"Rotation must be 90, 180, or 270, was ${rotation}"
                rotated_offsets.append((-offset_y, offset_x))
        return rotated_offsets
