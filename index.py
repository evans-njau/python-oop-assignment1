# Base Class
class GameCharacter:
    def __init__(self, name, health, power):
        self.name = name
        self._health = health  # Encapsulation (protected attribute)
        self.power = power

    def attack(self):
        print(f"{self.name} attacks with power {self.power}!")

    def get_health(self):  # Encapsulated access
        return self._health

    def set_health(self, new_health):  # Setter with basic validation
        if new_health >= 0:
            self._health = new_health
        else:
            print("Health cannot be negative.")

    def display(self):
        print(f"Name: {self.name} | Health: {self._health} | Power: {self.power}")


# Inherited Class
class Wizard(GameCharacter):
    def __init__(self, name, health, power, magic_level):
        super().__init__(name, health, power)
        self.magic_level = magic_level

    def attack(self):
        print(f"{self.name} casts a spell with magic level {self.magic_level}!")

    def display(self):
        super().display()
        print(f"Magic Level: {self.magic_level}")


# Inherited Class
class Warrior(GameCharacter):
    def __init__(self, name, health, power, weapon):
        super().__init__(name, health, power)
        self.weapon = weapon

    def attack(self):
        print(f"{self.name} swings a {self.weapon} with power {self.power}!")

    def display(self):
        super().display()
        print(f"Weapon: {self.weapon}")


# Example usage
wizard = Wizard("Gandalf", 100, 50, "High")
warrior = Warrior("Aragorn", 120, 80, "Sword")

wizard.attack()
warrior.attack()

wizard.set_health(90)
warrior.set_health(-10)  # Invalid

wizard.display()
warrior.display()
