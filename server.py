import socket
from _thread import *
import pickle
import random

server = "192.168.1.11"
port = 5555

expected_players = 0
# cube_length = expected_players*15*3
cube_length = 135
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


def threaded_client(conn, player, exp_players, main_loop, cube1):
    cube_new = [cube1[i:i + 15] for i in range(0, len(cube1), 15)]
    pack = [player, cube_new[player]]
    msg = pickle.dumps(pack)
    conn.send(msg)


    reply = ""
    if player <= exp_players:
        main_loop = True
        while main_loop:
            try:

                data = pickle.loads(conn.recv(2048))

                if not data:
                    print("Disconnected")
                    break
                else:
                    # if player == 1:
                        # reply = players[0]
                    # else:
                        # reply = players[1]

                    print("Received: ", data)
                    print("Sending : ", reply)

                conn.sendall(pickle.dumps(reply))
            except:
                break

        print("Lost connection")
        conn.close()


currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer, expected_players, loop, cube))
    currentPlayer += 1