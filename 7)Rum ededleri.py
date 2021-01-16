values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
values2 = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
r2 = 0
r3 = ''
t = 1
r = input()

r = r.split('+')

for j in range(len(r)):
    for i in range(len(r[j])):
        r2 = r2 + values[r[j][i]]
        if i > 0:
            if values[r[j][i]] > values[r[j][i-1]]:
                r2 = r2 - 2 * values[r[j][i-1]] # For CIV. 100+10+50-20 = 100+40

while r2 > 0:
    for i in values2:
        if (r2 // i) > 3 and (r2 // i) <= 4: # For IV, XL, CD, etc.
            r3 = r3 + values2[i]
            r3 = r3 + values2[t]
            r2 = r2 - 4*i
        elif (r2 // i) >= 1:
            if (r2 // (t * 0.9)) >= 1 and (r2 // (t * 0.9)) < 2: # For CM, XC, IX, etc.
                r3 = r3 + values2[t*0.1]
                r3 = r3 + values2[t]
                r2 = r2 - t*0.9
            else: # For I, V, C, L, etc.
                while (r2 // i) >= 1: # For I, II, III, X, XX, CCC, etc.
                    r3 = r3 + values2[i]
                    r2 = r2 - i
        else:
            r2 = r2
        t = i

print(r3)
