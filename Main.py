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
    for i in range(1, length+1):
        RowFillTree.node(filledLengthsMap, boardNumbersMap, "", 0,i)
        print(i)
    if max(filledLengthsMap.keys()) == length:
        filledLengthsMap[length] = [row for row in filledLengthsMap[length] if "1" not in row]
    print(filledLengthsMap)
    print(node(board,boardNumbersMap,0,filledLengthsMap))
