from pet import *

class Cat(Pet):
    def __init__(self, name, type, tricks, noise):
        Pet.__init__(self, name, type, tricks, noise)

    def make_noise(self):
        print(self.noise)             