n = input().split()
t1 = int(n[0])
t2 = int(n[1])
t3 = int(n[2])
if t1 == 0 or t2 == 0 or t3 == 0:
    t = 0
else:
    t = (t1*t2*t3)/(t3*t2+t1*t3+ t2*t1)
print('%.2f' %t)
