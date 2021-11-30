n=int(input())
x=0
if n==0:
    print(1)
else:
    while n>0:
        n=n//10
        x=x+1
    print(x)
