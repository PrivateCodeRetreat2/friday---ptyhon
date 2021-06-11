import unittest

from approvaltests.approvals import verify


from approvaltests.reporters.generic_diff_reporter_factory import GenericDiffReporterFactory


class Board:
    def __init__(self):
        self.board = {}

    def print(self, printer):
        board =""
        for y in range(0,6):
            for x in range(0,6):
                if f"{x},{y}" in self.board:
                    board += "x "
                else:
                    board += ". "
            board += "\n"

        printer(board)

    def set_alive(self,x,y):
        self.board[f"{x},{y}"] = True

    def advance(self):
        new_board = { (3,1) }

        # see how many live neigbors

        # detirmine next cell

        self.board = new_board
        pass


class RegressionTest(unittest.TestCase):


    def test_empty_board(self):
        # make a board
        board = Board()
        # approve the board
        board.print(verify)

    def test_cell_can_be_alive(selfe):
        # Create board
        board = Board()
        board.set_alive(2,1)
        board.print(verify)


    def test_square_advances(selfe):
        # Create board
        board = Board()
        board.set_alive(2,1)
        board.advance()
        board.print(verify)

    def test_cell_with_two_neighbours_stays_alive(selfe):
        # Create board
        board = Board()
        board.set_alive(2, 1)
        board.set_alive(3, 1)
        board.set_alive(4, 1)
        board.advance()
        board.print(verify)

