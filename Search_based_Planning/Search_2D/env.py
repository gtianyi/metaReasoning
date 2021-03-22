"""
Env 2D
@author: huiming zhou
"""


class Env:
    def __init__(self, inFile):
        with open(inFile) as mapFile:
            self.col_range = int(mapFile.readline())
            self.row_range = int(mapFile.readline())

            self.xI = (-1, -1)
            self.xG = (-1, -1)

            # self.motions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                           # (1, 0), (1, -1), (0, -1), (-1, -1)]

            self.obs = set()

            for i in range(self.row_range):
                line = mapFile.readline()
                for j in range(self.col_range):
                    if line[j] == '#':
                        self.obs.add((j, i))
                        continue
                    if line[j] == '@':
                        self.xI = (j, i)
                        continue
                    if line[j] == '*':
                        self.xG = (j, i)

