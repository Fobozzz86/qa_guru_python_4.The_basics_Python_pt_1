# Делаем списки!

l = [1, 2, 3, "a", "b", "c", [4, 5, 6]]

print(l[0])
print(l[-1])

print(l[-1][0])

print(l[::-1])

# Функции списков

# добавить элемент в конец списка
l.append("new element")
# расширить список другим списком
l.extend(["elem", "another elem"])

len(l)
# развернуть список
l.reverse()
# перезаписать значение в 0 позиции
l[0] = 200

print(l)

# Множества

s1 = {1, 2, 3, 4, 5, 5, 5, 5, 5}
s2 = {1, 2, 5, 5}

print(s1)
print(s2)

s1.intersection(s2)

s3 = s2 - s1
print(s3)

print(list(set([1, 2, 3, 4, 5, 5, 5])))