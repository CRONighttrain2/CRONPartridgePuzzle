import time

from Board import Board

def node(board: Board, side_length_map: dict[int, int], count: int):
    available_side_lengths = get_available_side_lengths(side_length_map)
    next_open = board.get_next_opening()
    if len(available_side_lengths) == 0:
        board.print_board()
        print()
        return 1
    for length in available_side_lengths:
        if board.can_place(length, next_open):
            new_board = board.__copy__()
            new_map = side_length_map.copy()
            new_map[length] -= 1
            new_board.place_tile(length, next_open)
            count += node(new_board, new_map, 0)
    return count

def get_available_side_lengths(side_length_map: dict[int, int]) -> list[int]:
    output = []
    for key in side_length_map:
        if side_length_map[key] > 0:
            output.append(key)
    return output
