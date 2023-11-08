"""defining a class"""

class Pizza: 
    """class to represent pizza"""
    # attributes
    # syntax <name> : <type>
    size: str
    toppings: int
    gluten_free: bool

    def __init__(self, size_input: str, toppings_input: int, gf_input: bool):
        """CONSTRUCTOR"""
        self.size = size_input
        self.toppings = toppings_input
        self.gluten_free = gf_input
    #returns self

    def price(self, input_pizza:str):
        """method ot compute price of pizza"""
        if input_pizza.size == "large":
            cost: float = 6.25
        else:
            cost: float = 5.00
        cost += .75 * input_pizza.toppings
        if input_pizza.gluten_free:
         cost+= 1.00
        return cost
    
    def add_toppings(self, num_toppings: int):
        """update order with num_toppings"""
        self.toppings += num_toppings