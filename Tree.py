import time
from functools import reduce

import RowFillTree
from Board import Board

def node(board: Board, side_length_map: dict[int, int], count: int, filled_row_map: dict[int, list[str]]):
    available_side_lengths: list[int] = get_available_side_lengths(side_length_map)
    if len(available_side_lengths) == 0:
        board.print_board()
        return 1
    smallest_available_space: dict[str, int] = board.get_smallest_opening()
    if filled_row_map.keys().__contains__(smallest_available_space["len"]):
        valid_rows = [row for row in filled_row_map[smallest_available_space["len"]] if RowFillTree.valid_row(row, side_length_map) and (int(max(row)) <= board.length - smallest_available_space["y"])]
        for row in valid_rows:
            num_list = [int(num) for num in list(row)]
            board_copy: Board = board.__copy__()
            smallest_available_space_copy = smallest_available_space.copy()
            side_length_map_copy = side_length_map.copy()
            for val in num_list:
                side_length_map_copy[val] -= 1
                board_copy.place_tile(val, smallest_available_space_copy)
                smallest_available_space_copy["x"] += val
            count += node(board_copy, side_length_map_copy, 0, filled_row_map)
        return count
    else:
        for length in available_side_lengths:
            board_copy: Board = board.__copy__()
            if board_copy.place_tile_in_next_opening_if_can(length):
                side_length_map_copy = side_length_map.copy()
                side_length_map_copy[length] -= 1
                count += node(board_copy, side_length_map_copy, 0, filled_row_map)
        return count

def get_available_side_lengths(side_length_map):
    return [length for length in side_length_map.keys() if side_length_map[length] > 0]
