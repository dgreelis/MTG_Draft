import numpy as np
import random


class Game:
    def __init__(self):
        self.went = []
        self.pack_num = []
        self.ready = False
        self.moves = [None, None]
        self.cube = []
        self.pick_num = 0
        self.round_num = 0

    def create_cube(self, humans, AI):
        human_players = humans
        AI_players = AI
        total_players = human_players + AI_players
        cube_length = total_players * 15 * 3
        cube = [*range(1, cube_length+1, 1)]
        random.shuffle(cube)
        # separate cube into groups of 15 (cards)
        self.cube = [cube[i:i + 15] for i in range(0, len(cube), 15)]
        # indicate that no players have went (all 0s)
        self.went = np.zeros(total_players)
        # set which pack the players should receive to start (equal to their player number)
        for i in range(0, total_players):
            self.pack_num.append(i)

    def connected(self):
        return self.ready