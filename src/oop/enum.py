# -*- coding: utf-8 -*-


from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


# @unique装饰器可以帮助我们检查保证没有重复值。
@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print()

day1 = Weekday.Mon

print(day1)
print(Weekday.Tue)
print(Weekday['Wed'])
print(Weekday.Tue.value)
print(day1 == Weekday.Mon)

for name, member in Weekday.__members__.items():
    print(name, '=>', member)
