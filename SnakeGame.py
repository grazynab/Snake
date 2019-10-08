from Board import Board
from Console import Console
from GameState import GameState


class SnakeGame(object):

    def __init__(self):
        self.gameState = GameState.IN_PROGRESS
        self.board = Board()
        self.console = Console()

    def startGame(self):
        self.console.printStartMessage()
        while self.gameState == GameState.IN_PROGRESS:
            previousdir = self.board.direction
            self.board.direction = self.console.getMove()
            self.console.appearSnake(self.board.snake)
            self.console.appearFood(self.board.food)
            if self.board.isMoveValid(self.board.direction, previousdir):
                self.board.makeMove()
            self.console.appearSnake(self.board.snake)
            self.console.printGameInfo(self.board.score)
            if self.board.food.y == int(self.board.snake.y[0]) and self.board.food.x == int(self.board.snake.x[0]):
                self.board.snakeGrows()
                self.board.food = self.board.getNewFoodPosition(self.console.getRandomX(), self.console.getRandomY())
                self.console.appearFood(self.board.food)
                self.board.score += 1
            self.gameState = self.checkGameState()
        if self.gameState == GameState.OVER:
            self.console.screen.clear()
            self.console.printGameOverMessage(self.board.score)
            self.console.closeScreen()

    def checkGameState(self):
        if self.board.snakeHitsWall(self.console.screen.getmaxyx()):
            return GameState.OVER
        elif self.board.snakeHitsItself():
            return GameState.OVER
        else:
            return GameState.IN_PROGRESS

snake = SnakeGame()
snake.startGame()

