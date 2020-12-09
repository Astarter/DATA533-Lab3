from Animals.livestocks.livestock import Livestock


class Cow(Livestock):
    def __init__(self, owner, price=1000, weight=100):
        """
            param:
            owner: the name of the cow's owner.
            price: the price of the cow, in dollar.
            weight: the weight of the cow in kgs.

            the default weight for a cow is 100 kg.
            the default price for a  cow is 1000 dollars
        """

        Livestock.__init__(self, owner)
        self.price = price
        self.weight = weight

    def makeSound(self):
        print("Mooooooooooo!!!")

    def eat(self, food_amount):
        if food_amount < 0:
            print("Incorrect amount of food.")
        if food_amount > 1000:
            print("The max amount of food that a cow can eat at one time is 1000!")
            self.weight += (1000 / 100)
            print("1000 units of food added for this cow.")
        if 0 < food_amount <= 1000:
            self.weight += (food_amount / 100)
            print("%.2f amount of food is added for the cow" % food_amount)

    def getWeight(self):
        return self.weight

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price

    def display(self):
        Livestock.display(self)
        print("Price: $%.2f\nWeight: %.2f\n" % (self.price, self.weight))
