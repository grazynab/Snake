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
        self.food = self.getNewFoodPosition()
        self.snake = Coordinates([3, 3, 3], [3, 4, 5], ["X", "X", "X"])
        self.direction = Direction.DOWN
        self.score = 0

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

    def closeScreen(self):  # nigdzie tego nie użyłam
        curses.nocbreak()
        self.screen.keypad(False)
        curses.echo()
        curses.endwin()

    def getCharFromConsole(self):
        return self.screen.getch()

    def getRandomY(self):
        maxy = self.screen.getmaxyx()
        return random.randint(1, maxy[0] - 2)

    def getRandomX(self):
        maxx = self.screen.getmaxyx()
        return random.randint(1, maxx[1] - 1)

    def getNewFoodPosition(self):
        return Coordinates(self.getRandomX(), self.getRandomY(), "*")

    def appearFood(self):
        self.screen.addstr(self.food.y, self.food.x, self.food.shape)

    def appearSnake(self):
        for index, item in enumerate(self.snake.shape):
            self.screen.addstr(self.snake.y[index], self.snake.x[index], str(item))

    def makeMove(self):
        self.appearSnake() #nie jestem pewna, czy to powinno być tutaj
        self.appearFood()
        char = self.getCharFromConsole()
        # print doesn't work with curses, use addstr instead
        # 1. poierz znak od gracza
        # 2. wprowadz zmiany w tablicy gry
        # 3. wyswietl tablice na konsoli
        self.screen.clear()
        self.screen.border()
        if char == ord('q'):
            self.screen.addstr(0, 0, 'quit game')
        elif char == curses.KEY_RIGHT:
            self.direction = Direction.RIGHT
            self.moveRight()

        elif char == curses.KEY_LEFT:
            self.direction = Direction.LEFT
            self.moveLeft()

        elif char == curses.KEY_UP:
            self.direction = Direction.UP
            self.moveUp()

        elif char == curses.KEY_DOWN:
            self.direction = Direction.DOWN
            self.moveDown()

        self.appearSnake()
        self.printGameInfo()

    def moveRight(self):
        if self.direction != Direction.LEFT:
            self.snake.y.insert(0, self.snake.y[0])
            self.snake.x.insert(0, self.snake.x[0] + 1)
            del self.snake.y[-1]
            del self.snake.x[-1]
        else:
            pass

    def moveLeft(self):
        if self.direction != Direction.RIGHT:
            self.snake.y.insert(0, self.snake.y[0])
            self.snake.x.insert(0, self.snake.x[0] - 1)
            del self.snake.y[-1]
            del self.snake.x[-1]
        else:
            pass

    def moveUp(self):
        if self.direction != Direction.DOWN:
            self.snake.y.insert(0, self.snake.y[0] - 1)
            self.snake.x.insert(0, self.snake.x[0])
            del self.snake.y[-1]
            del self.snake.x[-1]
        else:
            pass

    def moveDown(self):
        if self.direction != Direction.UP:
            del self.snake.y[-1]
            del self.snake.x[-1]
            self.snake.y.insert(0, self.snake.y[0] + 1)
            self.snake.x.insert(0, self.snake.x[0])
        else:
            pass

    def snakeEatsFood(self):
        self.snake.shape.append("X")
        if self.direction == Direction.LEFT:
            self.snake.x.append(self.snake.x[-1] + 1)
            self.snake.y.append(self.snake.y[-1])
        elif self.direction == Direction.RIGHT:
            self.snake.x.append(self.snake.x[-1] - 1)
            self.snake.y.append(self.snake.y[-1])
        elif self.direction == Direction.UP:
            self.snake.x.append(self.snake.x[-1])
            self.snake.y.append(self.snake.y[-1] + 1)
        elif self.direction == Direction.DOWN:
            self.snake.x.append(self.snake.x[-1])
            self.snake.y.append(self.snake.y[-1] - 1)
        self.food = self.getNewFoodPosition()
        self.appearFood()
        self.score += 1

    def printGameInfo(self):
        self.screen.addstr(0, 150, "Score: " + str(self.score))
        # self.screen.addstr(0, 150, "Screensize: " + str(self.screen.getmaxyx())) #13 x 168

    def snakeHitsWall(self):
        maxyx = self.screen.getmaxyx()
        if self.snake.x[0] == maxyx[1]:
            return True
        elif self.snake.x[0] == 0:
            return True
        elif self.snake.y[0] == maxyx[0] - 1:
            return True
        elif self.snake.y[0] == 0:
            return True
        else:
            return False

    def snakeHitsItself(self):
        for y, x in zip(self.snake.y[1:], self.snake.x[1:]):
            if y == self.snake.y[0] and x == self.snake.x[0]:
                return True

    def checkGameState(self):
        if self.snakeHitsWall():
            return GameState.OVER
        elif self.snakeHitsItself():
            return GameState.OVER
        else:
            return GameState.IN_PROGRESS

    def printStartMessage(self):
        self.screen.addstr(1, 1, "Direct the snake towards the food using arrows."
                                 "\nWatch out, don't hit the walls or bite your own body."
                                 "\nGood luck!")

    def printGameOverMessage(self):
        self.screen.addstr(5, 5, "GAME OVER! Your score is " + str(self.score))
