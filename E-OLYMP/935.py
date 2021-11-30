n=int(input())
if n<0:
    n=-n
    a=int(n/100)
    b=n%100
    c=int(b/10)
    d=n%10
    print(a)
    print(c)
    print(d)
else:
    a=int(n/100)
    b=n%100
    c=int(b/10)
    d=n%10
    print(a)
    print(c)
    print(d)
