s_d = 0
n = input()
a = len(n)
if(int(a) % 2 == 1):
    s_d += 1
for i in range(0, int(a)//2):
    if(n[i] == n[a-(i+1)]):
        s_d += 1
print(s_d)
