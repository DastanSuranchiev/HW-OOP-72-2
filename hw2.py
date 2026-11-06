import random

class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength



    def greet(self):
        print(f"{self.name}: Приветствую тебя!")

    def attack(self):
        pass

    def rest(self):
        self.health += 100
        print(f"{self.name} отдыхает.")



class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print(f"{self.name} атакует: Банкай! Большое багровое ледяное кольцо лотоса")

class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print(f"{self.name} атакует: Огненный шар!")


class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print(f"{self.name} атакует: Призрачный удар!")



warrior = Warrior('Warrior', 1, 100, 100, 100)
mage = Mage('Mage', 1, 100, 100, 100)
assassin = Assassin("Assassin", 55, 100, 100, 100)
all_f = [warrior, mage, assassin]
ftr= str(input("выберите героя (Warrior/Mage/Assassin):"))

fighters = [ "Warrior", "Mage", "Assassin"]
fighters2 = [ "Warrior", "Mage", "Assassin"]
fighters_ability = 0
fighters2.remove(ftr)

enemy = random.choice(fighters2)
print(f"ваш противник: {enemy}")

start = str(input("НАЧАТЬ ПОЕДИНОК? \n"
                  "(yes/no):"))

if start == "да":
    all_f[fighters.index(ftr)].attack()
    all_f[fighters.index(enemy)].attack()
    if all_f[fighters.index(ftr)].health  > all_f[fighters.index(enemy)].health:
        print("ваш боец выиграл")
    elif all_f[fighters.index(ftr)].health == all_f[fighters.index(enemy)].health:
        print("ничья")
    else:
        print("ваш боец проиграл")
else:
    print(f"вы признаете свое порожение. Победил {enemy}")



