import math
import random
import unittest

from Board import Board

class BoardCreationTests(unittest.TestCase):
    print("---------starting board creation tests---------")

    def test_size_0(self):
        print("-starting size 0 test")
        with self.assertRaises(ValueError) as assertion:
            b:Board = Board(0)
        self.assertEqual(type(assertion.exception), ValueError)

    def test_size_10(self):
        print("-starting size 10 test")
        b: Board = Board(10)
        self.assertTrue(len(b.board) == 10)
        self.assertTrue(len(b.board[0]) == 10)

    def test_size_negative(self):
        print("-starting random negative size test")
        size: int = (math.floor(random.random() * 100) + 1) * -1
        with self.assertRaises(ValueError) as assertion:
            b:Board = Board(size)
        self.assertEqual(type(assertion.exception), ValueError)

    def test_size_random(self):
        print("-starting random size test")
        for i in range(0, 10):
            size: int = math.floor(random.random() * 100) + 1
            print(f'--test iteration {i + 1} started, size = {size}')
            b: Board = Board(size)
            self.assertTrue(len(b.board) == size)
            self.assertTrue(len(b.board[0]) == size)

if __name__ == '__main__':
    creation_tests: unittest.TestSuite = unittest.TestLoader().loadTestsFromTestCase(BoardCreationTests)
    test_results = unittest.TestResult()
    creation_tests.run(test_results)
