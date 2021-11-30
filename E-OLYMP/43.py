a=input().split()
k=int(a[0])
m=int(a[1])
n=int(a[2])
d=int(a[3])


s=int((d*m*k*n)/(m*k*n-(m*n+k*n+m*k)))

if (s/k+s/m+s/n)==(s-d):
    if s==0:
        s=-1
    print(s)
    

else:
    s=-1
    print(s)
