class Player:
    def __init__(self, name):
        self.name = name
        self.energy = 100

    def use_energy(self, amount):
        if amount > 0:
            self.energy = max(0, self.energy - amount)

    def show_status(self):
        print(f"O'yinchi: {self.name}")
        print(f"Energiya: {self.energy}")


player = Player("Hero")
player.use_energy(35)
player.show_status()