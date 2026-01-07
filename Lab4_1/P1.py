'''
Natthida sriphan
663040479-3
P1
'''

from cat import Cat
from datetime import datetime, timedelta

cat1 = Cat("Jeno", "Ragdoll", 2, "Jaemin")
cat2 = Cat("Geto", "Persian", 2, "Gojo")
cat3 = Cat("Akasa", "Sphynx", 1, "Doma")

print(f"1st Cate Date In: {cat1.get_time_in()}") 
cat1.greet() 

print(f"2nd Cate Date Out: {cat2.get_time_out()}") 
new_date_out = datetime.now() + timedelta(days=2)
cat2.set_time_out(new_date_out)
print(f"2nd Cate Date Out: {cat2.get_time_out()}")

cat3.owner = "Patty" 
cat3.age = 5

cat1.print_cat()
cat2.print_cat()
cat3.print_cat()

print(f"Total number of cats in the class Cat so far : {Cat.get_num()}")

Cat.reset_cat()
print("Cat number in the class Cat has been reset.")

print(f"Total number of cats in the class Cat after reset: {Cat.get_num()}")