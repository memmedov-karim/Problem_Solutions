n = int(input())
i = 0
b = 0
while True:
    i += 1
    b = 2*b + i*(i + 1)/2
    if b >= n:
        break
print(i)
