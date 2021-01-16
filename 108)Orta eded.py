a,b,c=map(int,input().split())
m=max(a,b,c)
n=min(a,b,c)
if m>a and a>n:
    print(a)
elif m>b and b>n:
    print(b)
elif m>c and c>n:
    print(c)
