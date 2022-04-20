class Pizza:
    
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings
        
    def create(self):
        # answer
        pass

if __name__ == "__main__":
    machine = Pizza(["Regular", "Large"], ["Pepperoni", "Mushroom", ("Mushroom", "Extra Cheese"), ("Onion", "Pepperoni", "Green pepper"), "Fresh garlic", ("Green Pepper")])

    print(machine.create()) # output is ['Regular Pepperoni', 'Regular Mushroom', 'Regular Mushroom + Extra Cheese', 'Regular Onion + Pepperoni + Green pepper', 'Regular Fresh garlic', 'Regular Green Pepper', 'Large Pepperoni', 'Large Mushroom', 'Large Mushroom + Extra Cheese', 'Large Onion + Pepperoni + Green pepper', 'Large Fresh garlic', 'Large Green Pepper']
