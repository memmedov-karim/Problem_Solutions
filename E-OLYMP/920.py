x,y,z=map(float,input().split())
a=max(x,y)
b=max(y,z)
c=x+y+z
d=min(a,b,c)
df=format( d,".2f" )
print(df)
