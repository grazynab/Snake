from Coordinates import Coordinates
from Direction import Direction


class Board(object):

    def __init__(self):
        self.food = Coordinates(25, 10, "*")
        self.snake = Coordinates([3, 3, 3], [3, 4, 5], ["X", "X", "X"])
        self.direction = Direction.DOWN
        self.score = 0

    def isMoveValid(self, currentdir, previousdir):
        if currentdir == Direction.DOWN and previousdir == Direction.UP:
            return False
        elif currentdir == Direction.UP and previousdir == Direction.DOWN:
            return False
        elif currentdir == Direction.LEFT and previousdir == Direction.RIGHT:
            return False
        elif currentdir == Direction.RIGHT and previousdir == Direction.LEFT:
            return False
        else:
            return True

    def makeMove(self):
        if self.direction == Direction.RIGHT:
            self.moveRight()
        elif self.direction == Direction.LEFT:
            self.moveLeft()
        elif self.direction == Direction.UP:
            self.moveUp()
        elif self.direction == Direction.DOWN:
            self.moveDown()

    def moveRight(self):
        self.snake.y.insert(0, self.snake.y[0])
        self.snake.x.insert(0, self.snake.x[0] + 1)
        del self.snake.y[-1]
        del self.snake.x[-1]

    def moveLeft(self):
        self.snake.y.insert(0, self.snake.y[0])
        self.snake.x.insert(0, self.snake.x[0] - 1)
        del self.snake.y[-1]
        del self.snake.x[-1]

    def moveUp(self):
        self.snake.y.insert(0, self.snake.y[0] - 1)
        self.snake.x.insert(0, self.snake.x[0])
        del self.snake.y[-1]
        del self.snake.x[-1]

    def moveDown(self):
        del self.snake.y[-1]
        del self.snake.x[-1]
        self.snake.y.insert(0, self.snake.y[0] + 1)
        self.snake.x.insert(0, self.snake.x[0])

    def getNewFoodPosition(self, x, y):
        return Coordinates(x, y, "*")

    def snakeGrows(self):
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

    def snakeHitsWall(self, maxyx):
        if self.snake.x[0] == maxyx[1] - 1:
            return True
        elif self.snake.x[0] == 0:
            return True
        elif self.snake.y[0] == maxyx[0] - 1:
            return True
        elif self.snake.y[0] == 0:
            return True

    def snakeHitsItself(self):
        for y, x in zip(self.snake.y[1:], self.snake.x[1:]):
            if y == self.snake.y[0] and x == self.snake.x[0]:
                return True
