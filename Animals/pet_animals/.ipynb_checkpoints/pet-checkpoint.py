class Pet:

    def __init__(self, name):
        self.name = name

    def intro(self):
        print("Hello, my name is {}, I'm your pet".format(self.name))

    def display(self):
        print("Pet's name: {}".format(self.name))
