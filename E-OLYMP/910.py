n=int(input())
a=list(map(float,input().split()))
s=0
k=0
m=a[n-1]
for i in range(0,n):
    if m<a[i]:
        m=a[i]
if m<=0:
    print("Not Found")
else:
    for i in a:
        if i>0:
            s=s+i
            k=k+1
            z=s/k
            zf=format( z,".2f" )
    print(zf)
