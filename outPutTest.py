from Animals.livestocks.cow import *
from Animals.pet_animals.cat import *

# Test for subpackage 1:
print("This is a test for subpackage1:")
Garfield = Cat("Garfield", "orange")
Garfield.display()
Garfield.sound()
Garfield.intro()
Garfield.sound()
Garfield.describe("lazy")
Garfield.feed(1)
Garfield.getWeight()
Garfield.on_a_diet(2)
Garfield.setWeight(5)

print("\n")

# Test for subpackage 2:
print("This is a test for subpackage1:")
c1 = Livestock("ben")
c2 = Cow("Tim", price=200, weight=10)

print("Livestock c1:")
c1.intoduce()
c1.display()


print("\n")

print("Cow c2:")
c2.intoduce()
c2.makeSound()
c2.display()

c2.eat(-10)
c2.eat(2000)
c2.eat(100)
print("The weight of the cow is %.2f kgs" % c2.getWeight())

c2.setPrice(1000)
print("The price for c2 is %.2f dollars " % c2.getPrice())

