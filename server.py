import socket
from _thread import *
import pickle
import random
import numpy as np


server = "192.168.1.11"
port = 5555

human_players = 2
AI_players = 0
total_players = human_players + AI_players
cube_length = (total_players)*15*3
cube = list(range(cube_length))
random.shuffle(cube)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
loop = False

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")


def trade_packs(player_num, recd_pack_p_num, recd_pack):
    pass


def threaded_client(conn, player, hum_players, tot_players, main_loop, cube1):
    cube_new = [cube1[i:i + 15] for i in range(0, len(cube1), 15)]
    played = 0
    pass_to = player
    allWent = np.zeros((tot_players,), dtype=int)
    pack = [player, pass_to, played, cube_new[player]]
    msg = pickle.dumps(pack)
    conn.send(msg)


    reply = ""
    # if player == hum_players:
    main_loop = True
    while main_loop:
        try:
            # whenever a pack is sent by a client
            data = pickle.loads(conn.recv(2048))
            # change that player's value to a 1 (to indicate they went)
            allWent[data[0]] = 1
            # when all players have gone...
            if allWent == np.ones(tot_players):
                # start "trade_packs"
                trade_packs(player, data[0], data[1])
                # then set all the Went values back to 0
                allWent = np.zeros(tot_players)


            if not data:
                print("Disconnected")
                break
            else:

               print("Received: ", data)
               print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()



currentPlayer = 1
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer, human_players, total_players, loop, cube))
    currentPlayer += 1