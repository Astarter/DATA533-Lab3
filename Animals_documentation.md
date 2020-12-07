# Documentation

## class **pet(name=None)**
Class for pet animals, which should have the following parameters and methods:

**Parameteres**: 
**name**: string value
Contains the name of the pet 

**Methods**:
Method | Desription |
--- | --- |
**intro()** | Returns pet introduction
**display()** | Returns pet information

## class **cat(name=None)**	
**cat** class inherits from **pet** class. 
Class for cats, which should have the following parameters and methods:

**Parameteres**: 
**Name**: string value
Contains the name of the pet 

**Methods**:
Method | Desription |
--- | --- |
**sound()**: | Returns cat sound
**describe(adj)**: | Returns cat’s activity with adjective labels on string adj
**feed(cans=1.0)**: | Adds weight to the cat depending on the quantity fed with cans on float cans
**getWeight()**: | Returns cat’s weight
**on_a_diet(kg_down)**: | Substracts weight to the cat with kg scale on float kg_down 
**setWeight(weight)**: | Sets the cat's weight on float weight

## class **livestock(owner=None)**	
Class for livestock animals, which should have the following parameters and methods:

**Parameteres**: 
**owner**: string value
Contains the owner of the livestock 

**Methods**:
Method | Desription |
--- | --- |
**introduce()**: | Returns livestock introduction
**display()**: | Returns livestock information

## class **cow(owner=None, price=None)**	
**cow** class inherits from **livestock** class. 
Class for cow, which should have the following parameters and methods:

**Parameteres**: 
**owner**: string value
Contains the owner of the cow.

**price**: float value
Contains the purchased price(dollars) of the cow. 

**weight**: float value
Contains the weight(in kg) of the cow.

**Methods**:
Method | Desription |
--- | --- |
**makeSound()**: | Returns cow sound
**setPrice(price)**: | Sets the cow’s purchased price on float price
**getPrice()**: | Gets the cow’s purchased price
**eat()**: | Give food for the cow to eat, 100units of food = 1 kg in weight. 
**getWeight()**: | returns the cow’s weight.
**display()**: | Returns cow information
