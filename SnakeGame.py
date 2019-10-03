from Board import Board
from GameState import GameState


class SnakeGame(object):

    def __init__(self):
        self.gameState = GameState.IN_PROGRESS
        self.board = Board()

    def startGame(self):
        self.board.printStartMessage()
        while self.gameState == GameState.IN_PROGRESS:
            self.board.makeMove()
            if self.board.food.y == int(self.board.snake.y[0]) and self.board.food.x == int(self.board.snake.x[0]):
                self.board.snakeEatsFood()
            self.gameState = self.board.checkGameState()
        if self.gameState == GameState.OVER:
            self.board.screen.clear()
            self.board.printGameInfo()

snake = SnakeGame()
snake.startGame()

