import socket
from _thread import *
import pickle
from game import Game
import numpy as np

server = "10.94.207.207"
#server = "192.168.1.22"
port = 5554
# player ID, goes up after each player joins
player_num = 0
# create a game object called game from the class Game in the file game.py   :)
game = Game()
# these will be replaced with input entry, so we don't have to change code each time we play
human_players = 2
AI_players = 0
total_players = human_players + AI_players
# create cube with # human players and # AI players
game.create_cube(human_players, AI_players)
# fancy socket, bind, server stuff
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((server, port))
except socket.error as e:
    str(e)
# this listens for up to 2 players, need to increase if i plan to have more!  maybe 8??
s.listen(2)
print("Waiting for a connection, Server Started")


# Helper Functions!! ##############################################################################
def check_all_went():
    # to check if everyone went, add 1 to counter for each player that went (from game.went variable).
    # if that number is equal to the number of players, then everyone went.  Then reset to 0s
    counter = 0
    for i in range(0, total_players):
        if game.went[i] == 1:
            counter += 1
            if counter == total_players:
                output = True
                print("all went!")
                # reset the went to zeros
                game.went = np.zeros(total_players)
                print(game.cube)
            else:
                output = False
    return output


def next_pick():
    # go to the next pick
    game.pick_num += 1
    # if the pick is after the 15 cards, go to the next round
    if game.pick_num == 15:
        game.pick_num = 0
        next_round()
    # give each player the next pack.
    for player in range(0, total_players):
        game.pack_num[player] += 1
        # the last player needs to become the first player
        if game.pack_num[player] > total_players-1:
            game.pack_num[player] = 0


def next_round():
    # once we've gone through a full round (all 15 cards), delete the empty packs from the cube.  that way, the
    # pack numbers will still align with the player numbers
    game.round_num += 1
    if game.round_num == 3:
        game_end()
    # remove the first index a number of times equal to the number of players
    else:
        for player in range(0, player_num):
           game.cube.pop(0)


def game_end():
    print("Draft has ended")
# Helper Functions!! ##############################################################################


def threaded_client(conn, player, game, total_players):
    conn.send(str.encode(str(player)))

    reply = ""
    while True:
        data = conn.recv(2048).decode()

        if not data:
            break
        else:
            if data == "get":
                conn.sendall(pickle.dumps(game))
            else:
                # mark that the player went
                game.went[player] = 1
                print(game.went)
                # mark their response in the cube (turn it to a 0, so it is not an option to other players)
                game.cube[game.pack_num[player]][int(data)] = 0
                # see if everyone went.  if they did, start next pick
                all_went = check_all_went()
                if all_went:
                    next_pick()

    print("Lost connection")
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn, player_num, game, total_players))
    player_num += 1