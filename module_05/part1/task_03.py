import random

def action(warrior_1, warrior_2):
    dice = [1, 2]
    step = random.choice(dice)
    choice_warrior_1 = random.choice(dice)
    choice_warrior_2 = random.choice(dice)
    if choice_warrior_1 == 1:
        if choice_warrior_2 == 2:
            warrior_2.defend()
            warrior_1.attack(warrior_2)
        elif step == 1:
            warrior_1.attack(warrior_2)
            warrior_2.attack(warrior_1)
        else:
            warrior_2.attack(warrior_1)
            warrior_1.attack(warrior_2)
    else:
        warrior_1.defend()
        if choice_warrior_2 == 2:
            warrior_2.defend()
            print('Защищаемся! Ничего не происходит....')
        else:
            warrior_2.attack(warrior_1)
    warrior_1.guard, warrior_2.guard = 0, 0


class Warrior:

    def __init__(self, name):
        self.health = 100
        self.name = name
        self.armor = 100
        self.stamina = 100
        self.guard = 0

    def attack(self, other):
        if self.stamina > 0:
            self.stamina -= 10
            if other.guard == 0 or other.armor <= 0:
                damage = random.randint(10, 30)
                print(f'{self.name} атаковал {other.name} на {damage} единиц здоровья!')
                other.health -= damage
            else:
                damage = random.randint(0, 20)
                damage_armor = random.randint(0, 10)
                print(f'{self.name} атаковал {other.name} на {damage} единиц здоровья!')
                other.health -= damage
                print(f'{other.name} теряет также {damage_armor} единиц брони!')
                other.armor -= damage_armor
        if other.health <= 10:
            print(f'{self.name} победил!')

    def defend(self):
        self.guard = 1
        print(f'{self.name} защищается...')

    def __str__(self):
        return f'У {self.name}а осталось {self.health} здоровья и {self.armor} брони! '


soldier = Warrior('Пчелик')
knight = Warrior('Чел')

while soldier.health > 10 and knight.health > 10:
    action(soldier, knight)
    print(soldier, knight)
    print('----------')
