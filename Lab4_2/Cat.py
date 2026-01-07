'''
Natthida sriphan
663040479-3
Cat
'''

from datetime import datetime
class Cat:
    species = "Felis catus"
    total_cats = 0
    average_lifespan = 15

    def __init__(self, name, age, breed, color, weight=4):
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color
        self.weight = weight 

        self.hungry = False
        self.energy = 100
        self.happiness = 100

        Cat.total_cats += 1

    def meow(self):
        if self.hungry:
            return f"{self.name}: Meooow!! I'm hungry /ᐠ≽•ヮ•≼マ"
        elif self.energy < 30:
            return f"{self.name}: meow... I'm tired /ᐠﹷ ‸ ﹷ ᐟ\ﾉ"
        else:
            return f"{self.name}: Meow! ≽^•⩊•^≼"

    def eat(self, food_amount):
        if food_amount > 0:
            self.hungry = False
            self.energy = min(100, self.energy + food_amount * 2)
            self.happiness = min(100, self.happiness + 5)

    def play(self, play_time):
        self.energy = max(0, self.energy - play_time * 5)
        self.happiness = min(100, self.happiness + play_time * 3)
        if self.energy < 30:
            self.hungry = True

    def sleep(self, hours):
        self.energy = min(100, self.energy + hours * 10)
        self.hungry = True

    def get_status(self):
        return {
            "name": self.name,
            "age": self.age,
            "energy": self.energy,
            "happiness": self.happiness,
            "hungry": self.hungry
        }

    @classmethod
    def from_birth_year(cls, name, birth_year, breed, color, weight=4):
        current_year = datetime.now().year
        age = current_year - birth_year
        return cls(name, age, breed, color, weight)

    @classmethod
    def get_species_info(cls):
        return f"Species: {cls.species}, Average lifespan: {cls.average_lifespan} years"

    @staticmethod
    def is_senior(age):
        return age > 7

    @staticmethod
    def calculate_healthy_food_amount(weight):
        return weight * 20  # grams
