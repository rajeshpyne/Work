''':cvar
Software entities(Classes, modules, functions) should be open for extension, not modification.

Let’s imagine you have a store, and you give a discount of 20% to your favorite customers using this class:
When you decide to offer double the 20% discount to VIP customers. You may modify the class like this:
'''
from dataclasses import dataclass
from abc import ABC, abstractmethod


class Discount(ABC):

    @abstractmethod
    def get_discount(self):
        pass


@dataclass
class NonOCD_Discount(Discount):
    customer: str
    price: float

    def get_discount(self):
        if self.customer == 'normal':
            return self.price * 0.2
        if self.customer == 'vip':
            return self.price * 0.4

''':cvar
If we want to give a new percent discount maybe, to a different type of customers, 
you will see that a new logic will be added.
'''

@dataclass
class RealDiscount(Discount):
    customer: str
    price: float

    def get_discount(self):
        return self.price * 0.2

''':cvar
To make it follow the OCP principle, we will add a new class that will extend the Discount.
'''
# Extension without modification.
class VIPDiscount(RealDiscount):

    def get_discount(self):
        return super().get_discount() * 2


if __name__=='__main__':

    rd = VIPDiscount('vip',40)
    x=rd.get_discount()
    print(x)