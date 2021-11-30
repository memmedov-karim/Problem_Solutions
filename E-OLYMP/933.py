n=int(input())
if n<0:
    n=-n
    a=int(n/10)
    b=n%10
    print(a+b)
else:
    a=int(n/10)
    b=n%10
    print(a+b)
