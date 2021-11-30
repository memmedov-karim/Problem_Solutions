c=[]
n=int(input())
for i in range(n):
    a,b=[float(a) for a in input().split()]
    k=a+b
    kf=format( k,".0f" )
    c.append(kf)
for i in c:
    print(i)
