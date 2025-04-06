# -*- coding: utf-8 -*-
# @Author: Engeryu
# @Date:   2018-09-13 13:16:29
# @Last Modified by:   Engeryu
# @Last Modified time: 2025-04-06 22:30:26
# Actions possible du joueur sur le plateau:
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board()
    letter = "X"
    while game.empty_squares():
        if letter == "O":
            square = o_player.get_move(game)
            player = o_player.pseudonym
        else:
            square = x_player.get_move(game)
            player = x_player.pseudonym
        if game.make_move(square, letter):
            if print_game:
                print(game.text[game.language]["position_prompt"].format(player,    square + 1))
                game.print_board()
                print("")
            if game.current_winner:
                if print_game:
                    print(game.text[game.language]["win_message"].format(player))
                return letter
            letter = "O" if letter == "X" else "X"
    if print_game:
        print(game.text[game.language]["tie_message"])