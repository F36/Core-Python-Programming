import random

n = random.randint(2, 100)

list1 = []

for i in range(n):
    list1.append(random.randint(0, (2 ** 31) - 1))

list2 = random.sample(list1, random.randint(1, n))

print sorted(list2)
