n=int(input())
A=list(map(int,input().split()))
m=A[0]
k=A[n-1]
for i in range(0,n):
    if m>A[i]:
        m=A[i]
for i in range(0,n):
    if k<A[i]:
        k=A[i]
print(m+k)
