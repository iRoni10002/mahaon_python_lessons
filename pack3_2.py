class Animal:

    name = str()
    age = int()

class Predator(Animal):

    def bit(self, victim):
        if isinstance(victim, Mammal):
            victim.die(self)

class Tiger(Predator):

    pass

class Mammal(Animal):

    def die(self):
        del self

class Zebra(Mammal):

    pass

tiger = Tiger
zebra = Zebra

tiger.bit(tiger, zebra)

