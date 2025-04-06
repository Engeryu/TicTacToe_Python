# -*- coding: utf-8 -*-
# @Author: Engeryu
# @Date:   2018-09-13 09:37:44
# @Last Modified by:   Engeryu
# @Last Modified time: 2025-04-06 22:28:53
# Definition des joueurs:
class Player:
    def __init__(self, letter, game):
        self.letter = letter
        self.pseudonym = input(game.text[game.language]["pseudonym_prompt"].format(self.letter))
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(game.text[game.language]["move_prompt"].format(self.pseudonym))
            if square.lower() == "q":
                print("Quitting the game...")
                exit(0)
            try:
                val = int(square)
                if val < 1 or val > 9:
                    print(game.text[game.language]["invalid_input"])
                elif str(val) not in game.board:
                    print(game.text[game.language]["already_taken"])
                else:
                    valid_square = True
            except ValueError:
                print(game.text[game.language]["invalid_input"])
        return val - 1