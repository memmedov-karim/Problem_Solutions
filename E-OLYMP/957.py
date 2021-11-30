n=int(input())
a=int(n/100)
b=n%100
c=int(b/10)
d=n%10
k=(a+c+d)**0.5
kf=format( k,".3f" )
print(kf)
