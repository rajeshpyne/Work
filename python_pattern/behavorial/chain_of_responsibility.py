"""
Chain of Responsibility is behavioral design pattern that allows passing request along the chain of potential handlers
until one of them handles request.

The pattern allows multiple objects to handle the request without coupling sender class to the concrete classes of the
receivers. The chain can be composed dynamically at runtime with any handler that follows a standard handler interface.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler class.
    """
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Returning a handler from here will let us link handlers in a convenient way like this:
        # moneky.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


""" 
All concrete Handlers either handle a request or pass it to the next handler in the chain 
"""


class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == 'Banana':
            return "Monkey: I'll eat the {request}"
        else:
            return super().handle(request)


class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}"
        else:
            return super().handle(request)


class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "MeatBall":
            return f"Dog: I'll eat the {request}"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    """
    The client code is usually suited to work with a single handler.
    In most cases, it is not even aware that the handler is part of the chain.
    """

    for food in ["Nut","Banana","MeatBall"]:
        result = handler.handle(food)
        if result:
            print(f"{result}",end="")
        else:
            print(f"{food} is left untouched", end="")


if __name__ == '__main__':
    monkey = MonkeyHandler()
    dog = DogHandler()
    squirrel = SquirrelHandler()

    monkey.set_next(dog).set_next(squirrel)
    client_code(monkey)
    print()
    client_code(dog)