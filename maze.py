import math
from turtle import *
from algo import PrimsRandomized
import time
from tkinter import *
from PIL import Image

class RectMaze:

    def __init__(self, n=10, sideLen=10):
        self.n = n
        self.sideLen = sideLen

    def create_square(self):
        side = self.sideLen * 5
        x = - side / 2
        y = side / 2

        penup()
        goto(x, y)
        pendown()

        for i in range(4):
            forward(side)
            right(90)

    def create_grid(self):

        x = - (self.n * self.sideLen) / 2
        y = - x
        penup()
        goto(x, y)

        for row in range(self.n):
            for col in range(self.n):
                pendown()

                forward(self.sideLen)
                right(90)
                forward(self.sideLen)
                right(90)
                forward(self.sideLen)
                right(90)
                forward(self.sideLen)
                right(90)
                penup()

                forward(self.sideLen)
            y -= self.sideLen
            goto(x, y)

    def create_maze(self):

        pr = PrimsRandomized(n)
        mst = pr.prims_mst()

        x = - (self.n / 2) * self.sideLen
        y = - x
        penup()
        goto(x, y)

        for row in range(self.n):
            for col in range(self.n):
                node = row * self.n + col

                pendown()

                if mst[node][pr.TOP] == 1:
                    penup()

                forward(self.sideLen)
                right(90)
                pendown()

                if mst[node][pr.RIGHT] == 1 or node == self.n ** 2 - 1:
                    penup()

                forward(self.sideLen)
                right(90)
                pendown()

                if mst[node][pr.BOTTOM] == 1:
                    penup()

                forward(self.sideLen)
                right(90)
                pendown()

                if mst[node][pr.LEFT] == 1 or node == 0:
                    penup()

                forward(self.sideLen)
                right(90)

                penup()
                forward(self.sideLen)
            y -= self.sideLen
            penup()
            goto(x, y)


if __name__ == '__main__':
    pensize(2)
    hideturtle()
    speed(30)

    n = 25
    sideLen = 25

    rm = RectMaze(n, sideLen)
    rm.create_maze()

    done()