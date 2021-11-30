import math

r = float(input())
d = 0

for x in range(1, int(r)):
    d = int(d) + math.sqrt(r ** 2 - x ** 2)

d = int(d) * 4
print(d)
