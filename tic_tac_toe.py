import numpy as np


class tic_tac_toe(object):
    def __init__(self):
        self.board = np.full((3, 3), 2)

    def who_first(self):
        """Function to determine who plays first
        Args:

        Returns:
        Returns 1 if player 1 has won, or 0 if opponent
        """

        turn = np.random.randint(0, 2)
        if turn.mean() == 0:
            self.turn_monitor = 0
        elif turn.mean() == 1:
            self.turn_monitor = 1
        return self.turn_monitor

    def move(self, player, coord):
        if self.board[coord] != 2 or self.game_status != "In Progress" or \
                self.turn_monitor != player:
            raise ValueError("Incorrect move")
        self.board[coord] = player
        self.turn_monitor = 1 - player
