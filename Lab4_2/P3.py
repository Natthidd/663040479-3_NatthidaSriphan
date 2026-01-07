'''
Natthida sriphan
663040479-3
P3
'''

from VideoGame import VideoGame
p1 = VideoGame("Neo123", "Ninja")
p2 = VideoGame("Luna99", "Wizard")

p1.fight_monster("Slime", 2)
p1.fight_monster("Dragon", 5)

p2.collect_coins(50)
p2.take_damage(30)

print(p1.get_stats())
print(p2.get_stats())

party = VideoGame.create_party(["Max", "Anna", "John"], "Doctor")

print(VideoGame.get_server_stats())
print(VideoGame.get_leaderboard())
