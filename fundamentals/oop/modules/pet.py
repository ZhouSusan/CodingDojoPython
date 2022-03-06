class Pet:
    health = 100
    energy = 70

    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.noise = noise

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def make_noise(self):
        print(self.noise)

snicker = Pet("snickers", "Shih Tzu", "fast speester", "woof")
sox = Pet("Sox", "cat", ["hide and seek", "climbs and jumps very high", "hunts fast"], "moew") 