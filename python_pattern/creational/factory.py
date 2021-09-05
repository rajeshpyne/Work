"""
Problem :
Say you're making software for an insurance company which offers insurance to people who're employed full-time.
You've made the application using a class called Worker.

However, the client decides to expand their business and will now provide their services to unemployed people as well,
albeit with different procedures and conditions.

Now you have to make an entirely new class for the unemployed, which will take a completely different constructor!
But now you don't know which constructor to call in a general case, much less which arguments to pass to it.

You can have some ugly conditionals all over your code where every constructor invocation is surrounded by if
statements, and you use some possibly expensive operation to check the type of the object itself.

If there are errors during initialization, they're caught and the code is edited to do that at every of the hundred
places the constructors are used at.

Without stressing it out to you, you're well aware that this approach is less than desirable, non-scalable and
all-around unsustainable.

Alternatively, you could consider the Factory Pattern.
Solution
Factories are used to encapsulate the information about classes we're using, while instantiating them based on certain
parameters we provide them with.

By using a factory, we can switch out an implementation with another by simply changing the parameter that was used to
decide the original implementation in the first place.

This decouples the implementation from the usage in such a way that we can easily scale the application by adding new
implementations and simply instantiating them through the factory - with the exact same codebase.

If we just get another factory as a parameter, we don't even need to know which class it produces. We just need to have
a uniform factory method which returns a class guaranteed to have a certain set of behaviors. Let's take a look.
"""

from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def calculate_risk(self):
        pass


class Worker(Product):
    def __init__(self, name, age, hours):
        self.name = name
        self.age = age
        self.hours = hours

    def calculate_risk(self):
        return self.age + 100 / self.hours

    def __repr__(self):
        return self.name + " [" + str(self.age) + "] - " + str(self.hours) + "h/week"


class Unemployed(Product):
    def __init__(self, name, age, able):
        self.name = name
        self.age = age
        self.able = able

    def calculate_risk(self):
        if self.able:
            return self.age + 10
        else:
            return self.age + 30

    def __repr__(self):
        if self.able:
            return self.name + " [" + str(self.age) + "] - able to work"
        else:
            return self.name + " [" + str(self.age) + "] - unable to work"


class PersonFactory:
    @staticmethod
    def get_person(type_of_person):
        if type_of_person == "worker":
            return Worker("Ajay", 22, 40)
        elif type_of_person == "unemployed":
            return Unemployed("Ajay", 22, False)


if __name__ == "__main__":
    factory = PersonFactory()
    product1 = factory.get_person("worker")
    print(product1)

    product2 = factory.get_person("unemployed")
    print(product2)
