n=int(input())
x=0
for i in range(1,n+1):
    if int(n/i)==n%i:
        x=x+1
print(x)
