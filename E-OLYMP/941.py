n=int(input())
if n<0:
    n=-n
    k=int(n/100)
    d=n%100
    f=int(d/10)
    e=n%10
    K=k*f*e
    M=k+f+e
    print(K-M)
else:
    k=int(n/100)
    d=n%100
    f=int(d/10)
    e=n%10
    K=k*f*e
    M=k+f+e
    print(K-M)
