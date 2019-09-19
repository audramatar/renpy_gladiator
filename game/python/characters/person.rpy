init python:
    import random
    class Person(object):
        def __init__(self, name):
            self.alive = True
            self.name = name
            self.hp = 10
            self.ac = 10
            self.attack_bonus = 2
            # Damage 1d4
            self.damage_dice_amount = 1
            self.damage_dice = 4
            self.damage_bonus = 1

        def attack_object(self):
            damage = 0;
            attack = random.randint(1, 20) + self.attack_bonus
            for i in range(self.damage_dice_amount):
                damage += random.randint(1, self.damage_dice) + self.damage_bonus

            return {
                "name": self.name,
                "attack": attack,
                "damage": damage
            }

        def defend(self, attack_object):
            global combat_message
            combat_message = ""
            name = attack_object["name"]
            if attack_object["attack"] >= self.ac:
                combat_message += self.take_damage(attack_object["name"], attack_object["damage"])
            else:
                 combat_message += "[name] misses!"

        def take_damage(self, name, damage):
            self.hp -= damage
            if self.hp - damage > 0:
                self.hp -= damage
                return "{} does {} damage!".format(name, damage)
            else:
                self.hp = 0
                self.alive = False
                return "{} does {} damage! {} has died!".format(name, damage, self.name)
