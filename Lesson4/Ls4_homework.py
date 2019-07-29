#Класс Деньги для работы с денежными суммами.
#Один объект должен быть иметь два аттрибута: рубли и копейки.
#Объект должен иметь метод, возращающий эквивалент объекта только в копейках в виде целого числа.
#На экран объект должен выводится как "x руб. y коп." (есть специальный магический метод,
# отвечающий за то, как объект выводится на экран).
#Реализовать сложение, вычитание и операции сравнения между объектами деньгами (для этого
# есть специальные магические методы).

class Money:

    def __init__(self, rubles, penny = 0):
        self.rubles = rubles
        self.penny = penny

    def penny_count(self):
        return self.penny + self.rubles * 100

    @staticmethod
    def penny_to_money(penny):
        rubl = penny // 100
        pennies = penny % 100
        return Money(rubl, pennies)

    def __repr__(self):
        return str(self.rubles) + " руб. " + str(self.penny) + " коп."

    def __eq__(self, other):
        if (self.penny == other.penny) and (self.rubles == other.rubles):
            return True
        return False

    def __ne__(self, other):
        if (self.penny != other.penny) or (self.rubles != other.rubles):
            return True
        return False

    def __lt__(self, other):
        return self.penny_count() < other.penny_count()

    def __le__(self, other):
        return self.penny_count() <= other.penny_count()

    def __gt__(self, other):
        return self.penny_count() > other.penny_count()

    def __ge__(self, other):
        return self.penny_count() >= other.penny_count()

    def __add__(self, other):
        return Money.penny_to_money(self.penny_count() + other.penny_count())

    def __sub__(self, other):
        return Money.penny_to_money(self.penny_count() - other.penny_count())

m1 = Money(3, 30) # создаем объект равным 3 рублям и 30 копейкам

penny = m1.penny_count()

print('m1 в копейках равен {}'.format(penny))
# "m1 в копейках равен 330'

print(type(penny))
# int

m2 = Money(4, 95)

m3 = m1 + m2

print('Мы получили {}'.format(m3))
# на экране появится "Мы получили 8руб. 25 коп."

if m1 == m2:
    print('{} и {} равны'.format(m1, m2))
elif m1 > m2:
    print('{} больше чем {}'.format(m1, m2))
else:
    print('{} меньше чем {}'.format(m1, m2))

m4 = Money(8, 25)

if m4 == m3:
    print('{} и {} равны'.format(m4, m3))
elif m4 > m3:
    print('{} больше чем {}'.format(m4, m3))
else:
    print('{} меньше чем {}'.format(m1, m2))