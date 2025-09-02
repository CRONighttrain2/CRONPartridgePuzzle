import time

import RowFillTree
import Tree
from Board import Board
from Tree import node

if __name__ == '__main__':
    boardNumber: int = 9
    boardNumbersMap: dict[int, int] = dict()
    length:int = 0
    for num in range(1, boardNumber+1):
        boardNumbersMap[num] = num
        length += num
    board = Board(length)
    # we can speed up this program by having all the available options for all sizes of row pre-computed
    filledLengthsMap: dict[int, list[str]] = dict()
    for i in range(1, min(length+1,32)):
        print(i)
        RowFillTree.node(filledLengthsMap, boardNumbersMap, "", 0,i)
    print(filledLengthsMap)
