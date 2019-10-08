import os
import curses
from _curses import curs_set
from Direction import Direction
import random


class Console(object):

    def __init__(self):
        self.screen = self.initScreen()

    def initScreen(self):
        os.environ["TERM"] = "linux"
        os.environ["TERMINFO"] = "/etc/terminfo"
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)
        curs_set(False)
        # stdscr.timeout(5000)
        # stdscr.nodelay(1)
        return stdscr

    def closeScreen(self):
        curses.nocbreak()
        self.screen.keypad(False)
        curses.echo()
        curses.endwin()

    def getCharFromConsole(self):
        return self.screen.getch()

    def getMove(self):
        key = self.getCharFromConsole()
        self.screen.clear() #?
        self.screen.border() #?

        if key == curses.KEY_RIGHT:
            return Direction.RIGHT

        elif key == curses.KEY_LEFT:
            return Direction.LEFT

        elif key == curses.KEY_UP:
            return Direction.UP

        elif key == curses.KEY_DOWN:
            return Direction.DOWN

    def getRandomY(self):
        maxy = self.screen.getmaxyx()
        return random.randint(1, maxy[0] - 2)

    def getRandomX(self):
        maxx = self.screen.getmaxyx()
        return random.randint(1, maxx[1] - 2)

    def appearFood(self, food):
        self.screen.addstr(food.y, food.x, food.shape)

    def appearSnake(self, snake):
        for index, item in enumerate(snake.shape):
            self.screen.addstr(snake.y[index], snake.x[index], str(item))

    def printGameInfo(self, score):
        self.screen.addstr(0, 150, "Score: " + str(score))

