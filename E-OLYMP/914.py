n=int(input())
c=[]
for i in range(n):
    n1=input().split()
    c.append(n1)


for j in range(n):
    print('%.4f %.4f' %((float(c[j][0])+float(c[j][1])),
    (float(c[j][0])*float(c[j][1]))))
