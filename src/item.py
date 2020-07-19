import random

class Item:
    def __init__(self, name):
        self.name = name
    #     self.description = description
    # def on_keep(self):
    #     print(f"You have gained {self.name}")
    # def on_leave(self):
    #     print(f"You have left {self.name}")

# class Weapon(Item):
#     def __init__(self, name, description, damage):
#         super().__init__(name, description)
#         self.damage = damage
#     def attack(self):
#         print(random.randrange(1, self.damage))

# class Healing(Item):
#     def __init__(self, name, description, healing):
#         super().__init__(name, description)
#         self.healing = healing

# Declare all items

# item = {
#     'sword': Weapon("Sword", "Trusty sword for close range protection against enemies.", 3),
#     'aide': Healing("First aid kit", "Sack filled with bandages, gauze, and ointments to treat wounds.", 2),
#     'mushrooms': Healing("Magic Mushrooms", "Natural remedy that is a magic cure all and also provides nutrients.", 4),
#     'flashlight': Item("Flashlight", "Neccissity for your travels through caves."),
#     'satchel': Item("Empty satchel of gold", "Empty satchel that once held gold treasure.")
# }