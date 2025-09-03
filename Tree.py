import time

import RowFillTree
from Board import Board

def node(board: Board, side_length_map: dict[int, int], count: int, filled_row_map: dict[int, list[str]]):
    #if we can't place anything then we have found a solution
    available_side_lengths = get_available_side_lengths(side_length_map)
    if len(available_side_lengths) == 0:
        board.print_board()
        print()
        return 1
    available_space = board.get_amount_of_open_space()
    #if we have computed all possible variations for the next open row on the board, iterate through those
    if filled_row_map.keys().__contains__(available_space):
        for row in filled_row_map[available_space]:
            if RowFillTree.valid_row(row, side_length_map):
                new_board = board.__copy__()
                for char in row:
                    new_board.place_tile_in_next_opening_if_can(int(char))
                new_map = side_length_map.copy()
                row_count = RowFillTree.get_number_count_in_row(row)
                for key in row_count:
                    new_map[key] -= row_count[key]
                count += node(new_board, new_map, 0,filled_row_map)
        return count
    #if we haven't computed the possible variations for the next opening iterate through every possible block we can place
    else:
        next_open = board.get_next_opening()
        for length in available_side_lengths:
            # filter out any case where the 1 is on the sides of the board as they cannot happen
            if length == 1 and ((next_open["y"] == 0 or next_open["y"] == (board.length - 1)) or (next_open["x"] == 0 or next_open["x"] == (board.length - 1))):
                continue
            if board.can_place(length, next_open):
                new_board = board.__copy__()
                new_map = side_length_map.copy()
                new_map[length] -= 1
                new_board.place_tile(length, next_open)
                count += node(new_board, new_map, 0, filled_row_map)
        return count

def get_available_side_lengths(side_length_map: dict[int, int]) -> list[int]:
    output = []
    for key in side_length_map:
        if side_length_map[key] > 0:
            output.append(key)
    return output
