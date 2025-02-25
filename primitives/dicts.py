# Заводим словарики

d = {
    "key": "value",
    "another": "another value"
}

user1 = {
    "name": "Vasya",
    "age": 18,
}

user2 = {
    "name": "Petya",
    "age": 20,
}

users = {
    25: user1,
    42: user2
}

print(users[42])
print(user1["name"])
print(user2["name"])


users[55] = {"name": "Oleg", "age": 25}

print(users[55])
# Функции словарей

print("-----")
from pprint import pprint # более красвей форматирует
pprint(list(users.items()))

print("-----")
print(users.values())
print(users.keys())

# print(users[50])
print(users.get(50, {"name": "default user"}))
print(users.get(42, {"name": "default user"}))