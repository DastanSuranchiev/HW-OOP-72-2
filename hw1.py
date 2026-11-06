class Hero:
    def __init__(self, name, level, health, strength ):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength = self.strength - 1

    def rest(self):
        print(f"{self.name} отдыхает...")
        self.health = self.health + 1



Batman = Hero("Batman", 100, 5000, 90 )
Joker = Hero("Joker", 100, 8000, 50 )
Robin = Hero("Robin", 80, 3000, 60 )
Harlequin = Hero("Harlequin", 95, 2000, 80 )

Batman.greet()
Joker.greet()
Robin.greet()
Harlequin.greet()

Batman.attack()
Joker.rest()
Harlequin.attack()
Robin.rest()


print(Harlequin.strength)
print(Joker.health)
print(Batman.strength)
print(Robin.health)