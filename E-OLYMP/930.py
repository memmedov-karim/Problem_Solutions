n = input()
r = '0123456789'
say = 0
cavab = []

for i in r:
    if i not in n:
        say += 1
        cavab.append(i)


print(say)
print(*cavab, end='')
