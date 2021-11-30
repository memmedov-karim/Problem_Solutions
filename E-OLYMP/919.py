h=int(input())
n=list(map(float,input().split()))
s=0
k=0
c=[]
for i in range(h):
    if (i+1)%3==0:
        if n[i]>0:
            c.append(n[i])
            s=s+1
            k=sum(c)
print(s,format( k,".2f" ))
