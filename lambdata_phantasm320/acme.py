import random


class Product():
    def __init__(self, name, price=10, weight=20,
                 flammability=0.5,
                 identifier=random.randint(1000000, 10000000)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        if self.price / self.weight < 0.5:
            return 'Not so stealable...'
        elif self.price / self.weight >= 0.5 < 1.0:
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'

    def explode(self):
        if self.flammability * self.weight < 10:
            return 'fizzle.'
        elif self.flammability * self.weight >= 10 < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'


class BoxingGlove(Product):

    def __init__(self, name, price=10, weight=10,
                 flammability=0.5,
                 identifier=random.randint(1000000, 10000000)):
        super().__init__(name, price, weight,
                         flammability, identifier)

    def explode(self):
            return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif self.weight >= 5 < 15:
            return "Hey that hurt!"
        else:
            "OUCH!"
