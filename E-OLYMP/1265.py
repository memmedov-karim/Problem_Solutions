a=-1
b=-1
c=-1
d=[]
while a!=0 and c!=0 and b!=0:
    a,b,c=map(int,input().split())
    if a==0 and b==0 and c==0:
        d.append("")
    elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        d.append("right")
    else:
        d.append("wrong")
for i in d:
    print(i)
