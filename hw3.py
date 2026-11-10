from abc import ABC, abstractmethod

class Hero(ABC):
  def __init__(self, name, level, health, strength):
    self.name = name
    self.level = level
    self.__health = health
    self.strength = strength

  def greet(self):
    print(f"Привет, я {self.name}, мой уровень {self.level}")

  def rest(self):
    print(f"{self.name} отдыхает")
    self.__health += 1

  @abstractmethod
  def attack(self):
    pass


class Warrior(Hero):
  def attack(self):
    print(f"{self.name} атакует мечом")


class Mage(Hero):
  def attack(self):
    print(f"{self.name} использует магию")


class Assassin(Hero):
  def attack(self):
    print(f"{self.name} атакует из-под тишка")


warrior = Warrior("Ахилес", 57, 100, 20)
mage = Mage("Гендальф", 67, 70, 30)
assassin = Assassin("Каму", 90, 80, 25)

for i in (warrior, mage, assassin):
  i.greet()
  i.attack()
  i.rest()
  print()