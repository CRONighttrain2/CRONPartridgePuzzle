import time
from functools import reduce
from numbers import Number

import RowFillTree
import Tree
from Board import Board
from Tree import node

if __name__ == '__main__':
    board_number: int = 9
    available_square_lengths: dict[int, int] = dict()
    length:int = 0
    for num in range(1, board_number + 1):
        available_square_lengths[num] = num
        length += num
    board = Board(length)
    ## we can speed up this program by having all the available options for all sizes of row pre-computed
    filledLengthsMap: dict[int, list[str]] = dict()
    for i in range(1,20):
        RowFillTree.node(filledLengthsMap, available_square_lengths, "", 0,i)
        print(i)
    print(filledLengthsMap)
    board.print_board()
    print(Tree.node(board, available_square_lengths, 0, filledLengthsMap))
