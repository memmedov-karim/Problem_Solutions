n=int(input())
a=list(map(float,input().split()))
m=a[0]
for i in range(n):
    if m>=a[i]:
        m=a[i]
if m>2.5:
    print("Not Found")
else:
    for j in range(n):
        if a[j]<=2.5:
            print(j+1,format( a[j],".2f" ))
            break
