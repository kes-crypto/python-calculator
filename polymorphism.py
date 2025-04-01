class Smartphone:
    """
    A class representing a Smartphone with brand, model, and price attributes.
    """
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def call(self, number):
        print(f"Calling {number} from {self.model}...")
    
    def get_info(self):
        return f"{self.brand} {self.model} costs ${self.price}"

# Example usage
phone = Smartphone("Apple", "iPhone 15", 999)
print(phone.get_info())
phone.call("+1234567890")

# Inheritance
class Smartwatch(Smartphone):
    def __init__(self, brand, model, price, battery_life):
        super().__init__(brand, model, price)
        self.battery_life = battery_life
    
    def get_info(self):
        return f"{self.brand} {self.model} costs ${self.price} with {self.battery_life} hours battery life."

watch = Smartwatch("Apple", "Watch Series 9", 399, 18)
print(watch.get_info())

# Activity 2: Polymorphism Challenge
class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# Example usage
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()
