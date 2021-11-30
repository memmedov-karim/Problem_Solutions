v = 0
g = 0
s = int(input())
i = s

while(v <= 0.5):
    v = v + 1/i
    g += 1
    i = i - 1

print(s - g + 1)
