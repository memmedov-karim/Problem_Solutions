h=int(input())
n=list(map(float,input().split()))
m=n[0]
for i in range(0,h):
    if m>=n[i]:
        m=n[i]
print(2*m)
