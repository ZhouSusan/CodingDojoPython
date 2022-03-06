from pet import Pet
import cat

class Ninja:

    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self

    def feed(self, food_list):

        if len(food_list) > 0:
            print(f"Feeding {self.pet.name} {self.pet_food[-1]}!")
            food_list.pop()
            self.pet.eat()
        else:
            print("Oh no!! You need more pet food!")    
        return self

    def bathe(self):
        self.pet.make_noise() 

pet_food_list = ["Burger", "Pizza"]
maria = Ninja("Maria", "Fernadez", "soda bottles", pet_food_list, snicker)
maria.feed(pet_food_list).feed(pet_food_list).feed(pet_food_list).walk().bathe()

cat_food_list = ["catnips", "chicken bites"]
arthur = Ninja("Arthur", "Strobeck", "ball of string", cat_food_list, sox)
arthur.feed(cat_food_list).feed(cat_food_list).feed(cat_food_list).walk().bathe()
