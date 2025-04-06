# -*- coding: utf-8 -*-
# @Author: Engeryu
# @Date:   2018-09-13 10:02:58
# @Last Modified by:   Engeryu
# @Last Modified time: 2025-04-06 22:29:56
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from text import text

# Regle du jeu et definition du plateau:
class TicTacToe:
    def __init__(self, language):
        self.board = [str(i) for i in range(1, 10)]
        self.current_winner = None
        self.language = language
        self.text = text
    def print_board(self):
        for row in [self.board[i * 3 : (i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot not in ["X", "O"]]
    def empty_squares(self):
        return any(spot not in ["X", "O"] for spot in self.board)
    def make_move(self, square, letter):
        if self.board[square] not in ["X", "O"]:
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind * 3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False