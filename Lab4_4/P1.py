'''
Natthida Sriphan
663040479-3
P1
'''

from room import Bedroom, Kitchen

b1 = Bedroom(12, 10, 5)
print(b1.describe_room())
print("bed size:", b1.bed_size)
print("lighting:", b1.get_recommended_lighting())
print()

k1 = Kitchen(15, 12)
print(k1.describe_room())
i, w = k1.calculate_counter_space()
print("island:", i)
print("wall:", w)
print()

k2 = Kitchen(10, 8, False)
print(k2.describe_room())
i, w = k2.calculate_counter_space()
print("island:", i)
print("wall:", w)
