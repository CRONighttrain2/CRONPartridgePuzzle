import time

import Tree
from Board import Board
from Tree import node

if __name__ == '__main__':
    boardNumber: int = 9
    boardNumbersMap: dict = dict()
    length = 0
    for num in range(1, boardNumber+1):
        boardNumbersMap[num] = num
        length += num
    board = Board(length)
    print(node(board,boardNumbersMap,0))
