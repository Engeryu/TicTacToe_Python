# -*- coding: utf-8 -*-
# @Author: Engeryu
# @Date:   2018-09-21 08:07:34
# @Last Modified by:   Engeryu
# @Last Modified time: 2025-04-06 22:27:42

import shutil
import os
from src.board import TicTacToe
from src.player import Player
from src.game_rule import play
from src.text import text_language

# Choix de la langue:
language = input(text_language["text_language"])
# initialiser le jeu:
game = TicTacToe(language)
# Définir les joueurs et leur surnoms:
x_player = Player("X", game)
o_player = Player("O", game)
# Jouer au jeu:
play(game, x_player, o_player, print_game=True)

# À la fin du jeu, suppresion du dossier __pycache__
cache_dir = os.path.join(os.path.dirname(__file__), 'data', '__pycache__')
if os.path.exists(cache_dir):
    shutil.rmtree(cache_dir)