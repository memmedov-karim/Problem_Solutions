import math
a, h, z = input().split()
a = int(a)
h = int(h)
z = int(z)

c = z * math.pi / 180
d = math.sin(c) / math.cos(c)

if z == 90:
    c = a * h * math.sqrt(2)
elif 2 * h < a * d:
    c = (a * a / 2 - (a - h * math.sqrt(2) / d) ** 2 / 2) / math.cos(c)

else:
    c = a * a / 2 / math.cos(c)

print(format( c,".3f" ))
