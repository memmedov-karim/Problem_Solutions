n=int(input())
a=list(map(float,input().split()))
m=a[0]
for i in range(n):
    if m>=a[i]:
        m=a[i]
if m>=0:
    a.sort()
    print(format( a[n-1],".2f" ))
else:
    a.sort()
    print(format( abs(a[0]),".2f" ))
