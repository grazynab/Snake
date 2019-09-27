from Board import Board
from GameState import GameState


class SnakeGame(object):

    def __init__(self):
        self.gameState = GameState.IN_PROGRESS
        self.board = Board()

    def startGame(self):
        #print("Direct the snake towards the food using arrows."
            #"\nWatch out, don't hit the walls or bite your own body.\nGood luck!")

        while self.gameState == GameState.IN_PROGRESS:
            self.board.snakeMovement()
            self.board.chooseDirection()
            # self.board.checkGameState()


snake = SnakeGame()
snake.startGame()

