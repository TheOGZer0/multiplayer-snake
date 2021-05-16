from src.user.user import BaseUser
from src.ui.interface import Interface

import time

from pynput.keyboard import Key, Controller


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

    def play(self, wait: bool = False) -> None:
        """Event loop of the game, returns None

        Attributes:
            wait: Checks whether the game should ignore the wait after every iteration of the game loop.
        """
        while self.has_ended is False:
            try:
                while self.has_ended is False:
                    self.content()
                    if wait:
                        # TODO: This makes the thread always wait the same amount of time despite how long the frame has been shown.
                        # Wait for one frame
                        time.sleep(60/self.frames_per_second)
            except KeyboardInterrupt:
                if self.end_game() is True:
                    self.has_ended = True
                    break
                else:
                    continue

    def content(self) -> None:
        """This is the main code in which the game is executed, returns None

        The code for the game should be added to this method. Do not edit the play() method as it is only a wrapper
        for this method.
        """
        return None

    # TODO: Needs to be changed to work with server as well.
    def end_game(self, force: bool = False) -> bool:
        """Checks whether the game should be ended, returns boolean.

        Args:
            force: Checks if game should be ended without prompting the user.

        Returns:
            True if the game should be ended, false if not.
        """
        return_ = False
        if force is True:
            return_ = True
        else:
            user_input = self.validate_input(('y', 'n'))
            if user_input == 'y':
                return_ = True
            elif user_input == 'n':
                return_ = False
        return return_

    def validate_input(self, input_string: str, options: tuple[str]) -> str or None:
        """A method that wil check a string against a tuple, returns sting or None.

        Args:
            input_string: String to be validated.
            options: Tuple containing valid strings.

        Returns:
              Valid string if the input is valid, None if the input is invalid.
        """
        validated_string = None
        if input_string.lower().strip(' ') in [option.lower() for option in options]:
            validated_string = input_string.lower()
        else:
            self.interface.text_out(f"Please enter {options}")

        return validated_string
