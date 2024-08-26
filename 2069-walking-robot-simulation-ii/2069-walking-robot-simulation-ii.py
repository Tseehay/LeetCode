class Robot:

    def __init__(self, w, h):
        self.i = 0
        self.pos = [[0, 0, 'South']] + [[i, 0, 'East'] for i in range(1, w)] + \
            [[w - 1, i, 'North'] for i in range(1, h)] + \
            [[i, h - 1, 'West'] for i in range(w - 2, -1, -1)] +\
            [[0, i, 'South'] for i in range(h - 2, 0, -1)]

    def step(self, x):
        self.i += x

    def getPos(self):
        return self.pos[self.i % len(self.pos)][:2]

    def getDir(self):
        return self.pos[self.i % len(self.pos)][2] if self.i else 'East'


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
