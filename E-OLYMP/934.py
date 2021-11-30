a,b,c=map(int,input().split())
p=(a+b+c)
s=(p/2*(p/2-a)*(p/2-b)*(p/2-c))**0.5
ha=2*s/a
m=format( ha,".2f" )
hb=2*s/b
m1=format( hb,".2f" )
hc=2*s/c
m2=format( hc,".2f" )
print(m,m1,m2)
