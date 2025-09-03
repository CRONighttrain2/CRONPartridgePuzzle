from array import ArrayType

Black= "\u001b[30m"
Red= "\u001b[31m"
Green= "\u001b[32m"
Yellow= "\u001b[33m"
Blue= "\u001b[34m"
Magenta= "\u001b[35m"
Cyan= "\u001b[36m"
White= "\u001b[37m"
BrightBlack= "\u001b[90m"
BrightRed= "\u001b[91m"
BrightGreen= "\u001b[92m"
BrightYellow= "\u001b[93m"
BrightBlue= "\u001b[94m"
BrightMagenta= "\u001b[95m"
BrightCyan= "\u001b[96m"
BrightWhite= "\u001b[97m"
Reset= "\u001b[0m"

class Board:
    def __init__(self, length: int):
        self.length = length
        self.board: list[list[int]] = [None] * length
        for i in range (0, length):
            self.board[i] = [0] * length

    def __copy__(self):
        new_board = Board(self.length)
        new_board.board = [None] * self.length
        for i in range(0, self.length):
            new_board.board[i] = self.board[i].copy()
        return new_board

    def get_next_opening(self) -> dict[str, int]:
        for y in range(0, self.length):
            for x in range(0, self.length):
                if self.board[y][x] == 0:
                    return {"x": x,"y": y}
        return {"error":-1}

    def get_amount_of_open_space(self) -> int:
        opening: dict[str, int] = self.get_next_opening()
        for x in range(opening["x"], self.length):
            if self.board[opening["y"]][x] != 0:
                return  x - opening["x"]
        return self.length - opening["x"]

    def can_place(self, square_length: int, position: dict[str, int]) -> bool:
        if position.keys().__contains__("error"):
            return False
        if position["x"] + square_length > self.length or position["y"] + square_length > self.length:
            return False
        #due to filling this in from the bottom up and knowing that every position must be filled we only need to check the bottom most row for openings
        for x in range(position["x"], position["x"] + square_length):
            if self.board[position["y"]][x] != 0:
                return False
        return True

    def place_tile(self, square_length, position):
        for y in range(position["y"], position["y"] + square_length):
            for x in range(position["x"], position["x"] + square_length):
                self.board[y][x] = square_length

    #made so I don't have to call can_place/ get_next_opening in the tree, returns true if it can, false if it can't
    def place_tile_in_next_opening_if_can(self, square_length):
        next_open = self.get_next_opening()
        if next_open.keys().__contains__("error"):
            return False
        if not self.can_place(square_length, next_open):
            return False
        self.place_tile(square_length, next_open)
        return True

    def print_board(self) -> None:
        for row in self.board:
            rowOut = ""
            for character in row:
                if character == 0:
                    rowOut += Red
                if character == 1:
                    rowOut += Green
                if character == 2:
                    rowOut += BrightGreen
                if character == 3:
                    rowOut += Yellow
                if character == 4:
                    rowOut += BrightYellow
                if character == 5:
                    rowOut += Blue
                if character == 6:
                    rowOut += BrightBlue
                if character == 7:
                    rowOut += Magenta
                if character == 8:
                    rowOut += BrightMagenta
                if character == 9:
                    rowOut += White
                rowOut += str("■") + Reset
            print(rowOut)