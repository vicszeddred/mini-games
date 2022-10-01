from sysconfig import get_path_names

from pyrsistent import optional
import mini_games

games = [mini_games.magic8Ball]

def play_again(option):
    while option == "Y":


print("Welcome to 8-mini games game")
for game in games:
    print("{i}. {game}".format(i = range(len(games), game = game)))

option = input("Choose a game: ")
if str(option) == 1:
    mini_games.magic8Ball()