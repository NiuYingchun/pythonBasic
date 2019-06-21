'''
猩球崛起
'''


class Person:
    def __init__(self, name, atk, left):
        self.name = name
        self.atk = atk
        self.left = left

    def attack(self, starstar):
        starstar.left = starstar.left - self.atk

    def __str__(self):
        msg = '{}的攻击力是{}，剩余生命力{}'.format(self.name, self.atk, self.left)
        return msg


class StarSatr:
    def __init__(self, name, atk, left):
        self.name = name
        self.atk = atk
        self.left = left

    def attack(self, person):
        person.left = person.left - self.atk

    def __str__(self):
        msg = '{}的攻击力是{}，剩余生命力是{}'.format(self.name, self.atk, self.left)
        return msg


person = Person('诸葛亮', 10, 100)
print(person)
star1 = StarSatr('金刚', 20, 100)
print(star1)
print('----人攻击猩猩------')
person.attack(star1)
print(person)
print(star1)
print('------猩猩攻击人------')
star1.attack(person)
print(person)
print(star1)
