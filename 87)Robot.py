metn = input()
kordinat = [0]
s = 0

for i in metn:
    if i == "R":
        s += 1
        kordinat.append(s)

    elif i == "L":
        s -= 1
        kordinat.append(s)

print(len(set(kordinat)))
