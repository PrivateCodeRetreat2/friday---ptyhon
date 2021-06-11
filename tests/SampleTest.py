import unittest

from approvaltests.approvals import verify


from approvaltests.reporters.generic_diff_reporter_factory import GenericDiffReporterFactory


class Board:

    def print(self, printer):
        board =(". " * 6 + "\n") * 6
        printer(board)



class RegressionTest(unittest.TestCase):


    def test_empty_board(self):
        # make a board
        board = Board()
        # approve the board
        board.print(verify)

