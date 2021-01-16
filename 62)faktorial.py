f = 1
n = int(input())
for i in range(1, 100000):
    f = f * i
    if (f == n):
        print(i)
        break
