"""instantiating a class"""

# import the class
# from <file_name>.<module_name> import <class_name>
from lessons.classes.pizza import Pizza


my_pizza: Pizza = Pizza("large", 10, True) # constructor

# access/set/update attribute values
#my_pizza.size = "large"
#my_pizza.toppings = 10
#my_pizza.gluten_free = True

print("Size:")
print(my_pizza.size)
print(my_pizza.toppings)

#print("my_pizza:")
#print(my_pizza)

#print("Pizza class:")
#print(Pizza)

sals_pizza: Pizza = Pizza("medium", 5, True)
print(sals_pizza.size)

def price(input_pizza: Pizza) -> float:
    """compute the price of a pizza"""
    if input_pizza.size == "large":
        cost: float = 6.25
    else:
        cost: float = 5.00
    cost += .75 * input_pizza.toppings
    if input_pizza.gluten_free:
        cost+= 1.00
    return cost

# calling function
print(price(my_pizza))
print(price(sals_pizza))

# calling method
print(my_pizza.price())
print(sals_pizza.price())

my_pizza.add_toppings(3)
