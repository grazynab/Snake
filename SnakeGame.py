from Board import Board
from Console import Console
from GameState import GameState
from time import sleep


class SnakeGame:

    def __init__(self):
        self.gameState = GameState.IN_PROGRESS
        self.board = Board()
        self.console = Console()

    def startGame(self):
        print("\n\nDirect the snake towards the food using arrows."
              "\nWatch out, don't hit the walls or bite your own body."
              "\nGood luck!");
        sleep(6)
        while self.gameState == GameState.IN_PROGRESS:
            previousdir = self.board.direction
            self.console.prepareScreenForNextMove()
            self.board.direction = self.console.getMove()
            self.console.printSnake(self.board.snake)
            self.console.printFood(self.board.food)
            if self.board.isMoveValid(self.board.direction, previousdir):
                self.board.makeMove()
            self.console.printSnake(self.board.snake)
            self.console.printGameInfo(self.board.score)
            if self.board.isSnakeOnFood():
                self.board.growSnake()
                self.board.food = self.board.setNewRandomFoodPosition(self.console.getRandomX(), self.console.getRandomY())
                self.console.printFood(self.board.food)
                self.board.score += 1
            self.gameState = self.checkGameState()
        if self.gameState == GameState.OVER:
            self.console.clearScreen()
            self.console.closeScreen()
            print(">>> GAME OVER! Your score is " + str(self.board.score) + "<<<")

    def checkGameState(self):
        if self.board.doesSnakeHitWall(self.console.getMaxScreenSize()):
            return GameState.OVER
        elif self.board.doesSnakeHitItself():
            return GameState.OVER
        else:
            return GameState.IN_PROGRESS


snake = SnakeGame()
snake.startGame()
