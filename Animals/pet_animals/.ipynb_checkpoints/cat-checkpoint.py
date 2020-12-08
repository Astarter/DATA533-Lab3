from Animals.pet_animals.pet import Pet


class Cat(Pet):

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def sound(self):
        print("Meow meow prrrrrr")

    def describe(self, adj):
        print("{}, the {}, {} cat".format(self.name, adj, self.color))
