n=[int(i) for i in (input().split())]
if n[0]>=0.5*((n[1]**2+n[2]**2)**0.5):
    print('YES')
else:
    print('NO')
