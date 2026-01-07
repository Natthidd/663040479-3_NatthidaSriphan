'''
Natthida sriphan
663040479-3
P2
'''

from Cat import Cat
cat1 = Cat("Milo", 3, "Ragdoll", "White", 5)
cat2 = Cat.from_birth_year("Luna", 2015, "Persian", "Gray", 4)

print(cat1.meow())
cat1.play(10)
cat1.eat(20)
cat1.sleep(5)

print(cat2.meow())
cat2.play(15)

print(cat1.get_status())
print(cat2.get_status())

print(Cat.get_species_info())
print("Is Luna senior?", Cat.is_senior(cat2.age))
print("Recommended food for Milo:", Cat.calculate_healthy_food_amount(cat1.weight), "grams")

print("Total cats:", Cat.total_cats)
