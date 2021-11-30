N=int(input())
d=N
i=1
s=0
m=0
k=1
if N%10==0:
    print(format( 0,".3f" ))
else:
    while N>=1:
        N=N/10
        m=m+1
    while i<=m:
        s=s+int((d%(10**i))/10**(i-1))
        k=k*int((d%(10**i))/10**(i-1))
        i=i+1
        z=k/s
        zf=format( z,".3f" )
    print(zf)
