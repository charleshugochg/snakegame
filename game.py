from world import World, Direction
from display import Display
from controller import Controller
from pynput.keyboard import Key
from enum import Enum
import time

class Game:
    def __init__(self):
        self.__interval = 1
        self.__state = GameState.MENU
        self.world = World(10, 10)
        self.controller = Controller(self)
        self.display = Display()

    def run(self):
        start_time = time.time()
        while True:
            if time.time() - start_time > self.__interval:
                if self.__state == GameState.MENU:
                    self.__menu()
                elif self.__state == GameState.PLAYING:
                    self.__play()
                elif self.__state == GameState.RESTART:
                    self.world = World(10, 10)
                    self.__state = GameState.PLAYING    
                elif self.__state == GameState.GAMEOVER:
                    self.__over()
                elif self.__state == GameState.EXIT:
                    self.controller.listener.stop()
                    break

                start_time = time.time()

    def __play(self):
        # run once per interval
        if self.world.moveSnake():
            self.__state = GameState.GAMEOVER
        self.display.drawWorld(self.world.getWorld())

    def __over(self):
        self.display.drawGameover()

    def __menu(self):
        self.display.drawMenu()

    def handleEvent(self, event):
        if self.__state == GameState.MENU:
            if event == Key.enter:
                self.__state = GameState.RESTART
            elif event == Key.esc:
                self.__state = GameState.EXIT
        elif self.__state == GameState.PLAYING:
            if event == Key.up:
                self.world.changeSnakeDirection(Direction.UP)
            elif event == Key.down:
                self.world.changeSnakeDirection(Direction.DOWN)
            elif event == Key.right:
                self.world.changeSnakeDirection(Direction.RIGHT)
            elif event == Key.left:
                self.world.changeSnakeDirection(Direction.LEFT)
            elif event == Key.esc:
                self.__state = GameState.MENU
        elif self.__state == GameState.GAMEOVER:
            if event == Key.enter:
                self.__state = GameState.MENU
            elif event == Key.esc:
                self.__state = GameState.EXIT

class GameState(Enum):
    MENU = 1
    PLAYING = 2
    GAMEOVER = 3
    RESTART = 4
    EXIT = 5

game = Game()
game.run()