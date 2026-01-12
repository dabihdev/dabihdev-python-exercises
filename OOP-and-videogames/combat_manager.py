# A combat is basically a secondary game loop inside the main game loop
# You may implement a state machine to handle the states of the game:
# when the state is "BATTLE", then it starts the combat manager

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack_power = attack

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} took {damage} damage! Remaining HP: {max(0, self.health)}")

    def attack(self, target):
        print(f"{self.name} attacks {target.name}!")
        target.take_damage(self.attack_power)


class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start(self):
        print(f"--- A wild {self.enemy.name} appears! ---")
        
        while self.player.is_alive() and self.enemy.is_alive():
            self.player_turn()
            if self.enemy.is_alive():
                self.enemy_turn()
        
        self.resolve_victory()

    def player_turn(self):
        action = input(f"\n{self.player.name}'s turn! (A)ttack or (H)eal? ").lower()
        if action == 'a':
            self.player.attack(self.enemy)
        elif action == 'h':
            self.player.health += 20
            print(f"{self.player.name} healed 20 HP!")

    def enemy_turn(self):
        print(f"\n{self.enemy.name}'s turn...")
        self.enemy.attack(self.player)

    def resolve_victory(self):
        if self.player.is_alive():
            print(f"\nVictory! {self.enemy.name} has been defeated.")
        else:
            print(f"\nGame Over... {self.player.name} fell in battle.")


# Create characters
hero = Character("Aragorn", health=100, attack=25)
goblin = Character("Goblin Scout", health=50, attack=10)

# Start the encounter
encounter = Battle(hero, goblin)
encounter.start()