class Player:
    def __init__(self, name, score=0, level=1):
        self.name = name
        self.score = score
        self.level = level

    def add_points(self, points):
        self.score += points

    def level_up(self):
        self.level += 1

    def __str__(self):
        return f"{self.name} | Ball: {self.score} | Daraja: {self.level}"


player = Player("Ali")
player.add_points(100)
player.level_up()
print(player)
