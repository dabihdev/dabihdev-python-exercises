class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def to_dict(self):
        """Converts the item data into a dictionary for saving or UI display."""
        return self.__dict__

# --- Primary Child Classes ---

class Weapon(Item):
    def __init__(self, name, description, attack_power):
        super().__init__(name, description)
        self.attack_power = attack_power

class Potion(Item):
    def __init__(self, name, description, effect_type):
        super().__init__(name, description)
        self.effect_type = effect_type

class Key(Item):
    def __init__(self, name, description, room_code):
        super().__init__(name, description)
        self.room_code = room_code

# --- Secondary Child Class ---

class HealingPotion(Potion):
    def __init__(self, name, description, heal_amount):
        # We pass "Healing" as the effect_type to the Potion parent
        super().__init__(name, description, effect_type="Healing")
        self.heal_amount = heal_amount


# Creating the objects
rusty_sword = Weapon("Rusty Sword", "A chipped blade that has seen better days.", 5)
life_vial = HealingPotion("Life Vial", "A shimmering red liquid.", 20)

# Demonstrating to_dict()
print(f"You see: {rusty_sword.name}")
print(f"Description: {rusty_sword.description}")
print(f"Data: {rusty_sword.to_dict()}")