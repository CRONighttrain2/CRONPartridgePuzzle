import unittest

from Board import Board


class BlockPlacementTests(unittest.TestCase):
    print("--------- starting block placement tests---------")

    def test_place_1(self):
        print("-testing size 1 block placement")
        b: Board = Board(10)
        self.assertTrue(b.place_tile_in_next_opening_if_can(1))
        self.assertTrue(b.board[0][0] == 1)
        print()

    def test_place_4(self):
        print("-testing size 4 block placement")
        b: Board = Board(10)
        self.assertTrue(b.place_tile_in_next_opening_if_can(4))
        for y in range(0, 4):
            for x in range(0, 4):
                print(f'--testing ({y},{x})')
                self.assertTrue(b.board[y][x] == 4)
        print()

    def test_place_2_then_7(self):
        print("-testing size 2 block then size 7 block placement")
        b: Board = Board(10)
        self.assertTrue(b.place_tile_in_next_opening_if_can(2))
        print("-testing 2")
        for y in range(0, 2):
            for x in range(0, 2):
                print(f'--testing ({y},{x})')
                self.assertTrue(b.board[y][x] == 2)
        self.assertTrue(b.place_tile_in_next_opening_if_can(7))
        print("-testing 7")
        for y in range(0, 7):
            for x in range(2, 9):
                print(f'--testing ({y},{x})')
                self.assertTrue(b.board[y][x] == 7)
        print()

    def test_place_too_large(self):
        print("-testing placing a size 8 block on a size 4 board")
        b: Board = Board(4)
        self.assertFalse(b.place_tile_in_next_opening_if_can(8))
        print()

    def test_place_multiple_rows(self):
        print("-testing placing enough blocks to create multiple rows")
        b: Board = Board(4)
        self.assertTrue(b.place_tile_in_next_opening_if_can(2))
        self.assertTrue(b.place_tile_in_next_opening_if_can(2))
        self.assertTrue(b.place_tile_in_next_opening_if_can(1))
        for y in range(0, 2):
            for x in range(0, 4):
                self.assertTrue(b.board[y][x] == 2)
        self.assertTrue(b.board[2][0] == 1)
        print()

if __name__ == '__main__':
    unittest.main()
