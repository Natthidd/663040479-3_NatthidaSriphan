'''
Natthida sriphan
663040479-3
VideoGame
'''

from datetime import datetime
class VideoGame:
    total_players = 0
    difficulty_levels = ["Easy", "Medium", "Hard"]
    max_level = 100
    server_start_time = datetime.now()
    active_players = []
    leaderboard = {}

    def __init__(self, player_name, character_type):
        if not VideoGame.is_valid_character_name(player_name):
            raise ValueError("Invalid character name")

        self.player_name = player_name
        self.character_type = character_type
        self.level = 1
        self.health = 100
        self.exp = 0
        self.coins = 0
        self.inventory = []
        self.is_alive = True

        VideoGame.total_players += 1
        VideoGame.active_players.append(player_name)
        VideoGame.leaderboard[player_name] = 0

    def level_up(self):
        if self.level < VideoGame.max_level:
            self.level += 1
            self.health = 100
            VideoGame.leaderboard[self.player_name] = self.level * 100 + self.coins

        print(f"{self.player_name} leveled up!")
        print(f"Level: {self.level}, Health: {self.health}, Score: {VideoGame.leaderboard[self.player_name]}")

    def collect_coins(self, amount):
        self.coins += amount
        VideoGame.leaderboard[self.player_name] = self.level * 100 + self.coins
        print(f"{self.player_name} collected {amount} coins | Total coins: {self.coins} | Score: {VideoGame.leaderboard[self.player_name]}")

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.is_alive = False
            self.health = 0
            if self.player_name in VideoGame.active_players:
                VideoGame.active_players.remove(self.player_name)
            print(f"{self.player_name} has died (×_×)")
        else:
            print(f"{self.player_name} took {damage} damage | Health: {self.health}")

    def fight_monster(self, monster_name, monster_level):
        if not self.is_alive:
            print(f"{self.player_name} cannot fight, already dead.")
            return

        damage = VideoGame.calculate_damage(20, 5, monster_level)
        self.take_damage(damage)

        gained_exp = 10 * monster_level
        self.exp += gained_exp

        if self.is_alive:
            self.collect_coins(3 * monster_level)

        if self.exp >= VideoGame.calculate_exp_needed(self.level):
            self.exp = 0
            self.level_up()

        print(f"Fought {monster_name} (Lv {monster_level}) | EXP gained: {gained_exp}")

    def get_stats(self):
        return (
            f"Player: {self.player_name}\n"
            f"Type: {self.character_type}\n"
            f"Level: {self.level}\n"
            f"Health: {self.health}\n"
            f"EXP: {self.exp}\n"
            f"Coins: {self.coins}\n"
            f"Alive: {self.is_alive}\n"
            f"Rank: {VideoGame.get_rank_title(self.level)}"
        )

    @classmethod
    def create_party(cls, players, character_type):
        return [cls(name, character_type) for name in players]

    @classmethod
    def get_server_stats(cls):
        uptime = datetime.now() - cls.server_start_time
        return (
            f"Server Uptime: {uptime}\n"
            f"Total Players: {cls.total_players}\n"
            f"Active Players: {cls.active_players}\n"
            f"Leaderboard: {cls.leaderboard}"
        )

    @classmethod
    def get_leaderboard(cls):
        sorted_board = sorted(cls.leaderboard.items(), key=lambda x: x[1], reverse=True)
        result = "----- Leaderboard -----\n"
        for name, score in sorted_board:
            result += f"{name}: {score}\n"
        return result

    @classmethod
    def reset_server(cls):
        cls.total_players = 0
        cls.leaderboard.clear()
        cls.active_players.clear()
        cls.server_start_time = datetime.now()

    @staticmethod
    def calculate_damage(attack_power, defense, level):
        damage = (attack_power * level) - defense
        return max(0, damage)

    @staticmethod
    def calculate_exp_needed(level):
        return 100 * level

    @staticmethod
    def is_valid_character_name(name):
        return 3 <= len(name) <= 20 and name.isalnum()

    @staticmethod
    def get_rank_title(level):
        if level < 20:
            return "Beginner"
        elif level < 50:
            return "Warrior"
        elif level < 80:
            return "Elite"
        else:
            return "Legend"
