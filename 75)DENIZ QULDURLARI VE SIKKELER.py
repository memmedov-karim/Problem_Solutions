a,m=map(int,input().split())
d=(2*a+1)**2-4*(2*a-2-2*m)
n=(d**0.5-2*a-1)/2
nf=format( n,".0f" )
print(nf)
