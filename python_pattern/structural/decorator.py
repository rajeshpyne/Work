"""
Problem : Imagine you are making a video game. The core mechanic of your game is that the player can add different
power-ups mid-battle from a random pool.
Those powers can't really be simplified and put into a list you can iterate through, some of them fundamentally
overwrite how the player character moves or aims, some just add effects to their powers, some add entirely new
functionalities if you press something etc.

You might initially think of using inheritance to solve this. After all, if you have basic_player, you can inherit
blazing_player, bouncy_player, and bowman_player from it.

But what about blazing_bouncy_player, bouncy_bowman_player, blazing_bowman_player, and blazing_bouncy_bowman_player?

As we add more powers, the structure gets increasingly complex, we have to use multiple inheritance or repeat the code,
and every time we add something into the game it's a lot of work to make it work with everything else.

Solution : The Decorator Pattern is used to add functionality to a class without changing the class itself. The idea is
to create a wrapper which conforms to the same interface as the class we're wrapping, but overrides its methods.

It can call the method from the member object and then just add some of its own functionality on top of it, or it can
completely override it. The decorator(wrapper) can then be wrapped with another decorator, which works exactly the same.

This way, we can decorate an object as many times as we'd like, without changing the original class one bit. Let's go
ahead and define a Decorator

Reference :
https://github.com/faif/python-patterns/blob/master/patterns/structural/decorator.py
https://stackabuse.com/structural-design-patterns-in-python/#decorator
"""
from abc import ABC, abstractmethod


class PlayerDecorator(ABC):
    @abstractmethod
    def handle_input(self, c):
        pass


class BasePlayer:
    def __init__(self):
        pass

    def handle_input(self, c):
        if c == 'w':
            print("Move Forward")
        elif c == 'e':
            print("Attack")
        else:
            print("Undefined Command")


class BlazingPlayer(PlayerDecorator):
    def __init__(self, wrapee):
        self.wrapee = wrapee

    def handle_input(self, c):
        if c == 'e':
            print("Fire and ", end='')

            self.wrapee.handle_input(c)


class BowmanPlayer(PlayerDecorator):
    def __init__(self, wrapee):
        self.wrapee = wrapee

    def handle_input(self, c):
        if c == 'w':
            print("Jump and Move Forward", end='')

            self.wrapee.handle_input(c)


if __name__=='__main__':
    player = BasePlayer()
    player.handle_input('e')
    player.handle_input('w')

    player1 = BlazingPlayer(player)
    player1.handle_input('e')

    player2 = BowmanPlayer(player1)
    player2.handle_input('w')