from decimal import Decimal

a = 123

a = a + 456
a = a - 456
a = a / 456
a = a * 456
a = a ** 3 # возведение в степень
a = (100 + 200) / 300 * 400

a = 123456789123456789123456789123456789123456789123456789123456789123456789

a = 0b11001010010 # двоичное число
a = 0o1234567 # восьмиричное число
a = 0x1234567890abcdef # 16тиричное

a = 0.5
print(a)

a = 0.1 + 0.2
# ассерт не пройдет
# assert a == 0.3

# нормально решение проблемы, сдвинуть запятую умножением, а потом разделить
a = 0.1 * 10 + 0.2 * 10
b = a / 10
print(b)
assert b == 0.3


# Математика!

import math

print(math.pi)

# Рандом!
# так же есть библиотека Faker

import random

random.seed("some word")

print("-----------")

print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))

print("-----------")

print(round(1.333333, 2)) # округление до ... знаков после запятой