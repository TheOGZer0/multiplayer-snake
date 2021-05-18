import pynput.keyboard

from src.user.user import BaseUser
from src.ui.interface import Interface

import time


class Game:
    """A skeleton for a game

    This class should inherited by another class which should extend the content method. You use this class by invoking
    the play method which repeats the content method in a loop.

    Attributes:
        has_ended: Checks if the game has ended.
        players: List of players playing the game.
    """
    def __init__(self, players: list[BaseUser], interface: Interface, frames_per_second: int = 10):
        self.has_ended = False
        self.players = players
        self.interface = interface
        self.frames_per_second = frames_per_second

        self.key_listener = pynput.keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        )
        self.key_listener.start()

    def play(self, wait: bool = False) -> None:
        """Event loop of the game, returns None

        Attributes:
            wait: Checks whether the game should ignore the wait after every iteration of the game loop.
        """
        while self.has_ended is False:
            self.content()
            if wait:
                # TODO: This makes the thread always wait the same amount of time despite how long the frame has been shown.
                # Wait for one frame
                time.sleep(60/self.frames_per_second)

    def content(self) -> None:
        """This is the main code in which the game is executed, returns None

        The code for the game should be added to this method. Do not edit the play() method as it is only a wrapper
        for this method.
        """
        return None

    def on_press(self, key) -> None:
        """Shell for on press events, returns None

        This method can be inherited to fit the need of any game. Fires every time a key is pressed.

        Attributes:
            key: Required by pynput and automatically passed on.
        """
        print(key)
        return None

    def on_release(self, key) -> None:
        """Shell for on release events, returns None

        This method can be inherited to fit the need of any game. Fires every time a key is released.

        Attributes:
            key: Required by pynput and automatically passed on.
        """
        return None
