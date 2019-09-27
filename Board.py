import os
import curses
from _curses import curs_set

from Coordinates import Coordinates
from Direction import Direction
from FieldOption import fieldOption
from GameState import GameState

import random


class Board(object):

    def __init__(self):
        self.board = [[fieldOption.EMPTY for x in range(50)]] * 50
        self.screen = self.initScreen()
        self.food = Coordinates(self.getRandomNumber(), self.getRandomNumber(), "*")
        self.snake = Coordinates([3, 4, 5], [4, 4, 4], ["X", "X", "X"])
        self.direction = Direction.RIGHT
        self.appearFood()
        self.appearSnake()

    def initScreen(self):
        os.environ["TERM"] = "linux"
        os.environ["TERMINFO"] = "/etc/terminfo"
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)
        curs_set(False)
        stdscr.border()
        stdscr.timeout(5000)
        stdscr.nodelay(1)
        return stdscr

    def closeScreen(self):
        curses.nocbreak()
        self.screen.keypad(False)
        curses.echo()
        curses.endwin()

    def getCharFromConsole(self):
        return self.screen.getch()

    def getRandomNumber(self):
        return random.randint(0, min(self.screen.getmaxyx()))

    def newFoodPosition(self):
        self.food = Coordinates(self.getRandomNumber(), self.getRandomNumber(), "*")

    def appearFood(self):
        self.screen.addstr(self.food.y, self.food.x, self.food.shape)

    def appearSnake(self):
        for index, item in enumerate(self.snake.shape):
            self.screen.addstr(self.snake.y[index], self.snake.x[index], str(item))

    def snakeMovement(self):
        while self.direction == Direction.RIGHT:
            self.moveRight()
        while self.direction == Direction.LEFT:
            self.moveLeft()
        while self.direction == Direction.UP:
            self.moveUp()
        while self.direction == Direction.DOWN:
            self.moveDown()


        #że wąż sam idzie w aktywnym kierunku o pole (na x czasu?)

    def chooseDirection(self):
        #zmienić na wybór kierunku
        char = self.getCharFromConsole()
        # print doesn't work with curses, use addstr instead
        # 1. poierz znak od gracza
        # 2. wprowadz zmiany w tablicy gry
        # 3. wyswietl tablice na konsoli
        self.screen.clear()
        #self.printGameInfo()
        if char == ord('q'):
            self.screen.addstr(0, 0, 'quit game')
        elif char == curses.KEY_RIGHT:
            if self.direction != Direction.LEFT:
                self.direction = Direction.RIGHT
            else:
                pass
        elif char == curses.KEY_LEFT:
            if self.direction != Direction.RIGHT:
                self.direction = Direction.LEFT
            else:
                pass

        elif char == curses.KEY_UP:
            if self.direction != Direction.DOWN:
                self.direction = Direction.UP
            else:
                pass

        elif char == curses.KEY_DOWN:
            if self.direction != Direction.UP:
                self.direction = Direction.DOWN
            else:
                pass

        #rusza się cały wąż góra dół - zmienić to

    def moveRight(self):
    # for index, item in enumerate(self.snake.shape):
      #      self.screen.addstr(self.snake.y[index], self.snake.x[index] + 1, str(item))
        self.snake.x = [x + 1 for x in self.snake.x]
        self.appearSnake()

    def moveLeft(self):
        for index, item in enumerate(self.snake.shape):
            self.screen.addstr(self.snake.y[index], self.snake.x[index] - 1, str(item))
        self.snake.x = [x - 1 for x in self.snake.x]

    def moveUp(self):
        for index, item in enumerate(self.snake.shape):
            self.screen.addstr(self.snake.y[index] - 1, self.snake.x[index], str(item))
        self.snake.y = [y + 1 for y in self.snake.y]

    def moveDown(self):
        for index, item in enumerate(self.snake.shape):
            self.screen.addstr(self.snake.y[index] + 1, self.snake.x[index], str(item))
        self.snake.y = [y - 1 for y in self.snake.y]

    def printGameInfo(self):
        self.screen.addstr(0, 0, "Screensize: " + str(self.screen.getmaxyx()))
    #
    # def checkGameState(self):
    #     if Snake.hitWall():
    #         return GameState.OVER
    #     elif Snake.hitSnake():
    #         return GameState.OVER
    #     else:
    #         return GameState.IN_PROGRESS
    #
