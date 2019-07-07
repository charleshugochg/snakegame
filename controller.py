from pynput.keyboard import Key, Listener

class Controller:
    def __init__(self, game):
        self.__game = game
        self.listener = Listener(
            on_release = self.on_release)
        self.listener.start()

    def on_release(self, key):
        self.__game.handleEvent(key)

