x1,y1,x2,y2,x3,y3=map(float,input().split())
a=x2-x1
b=y2-y1
A=(a**2+b**2)**0.5
c=x3-x2
d=y3-y2
C=(c**2+d**2)**0.5
e=x3-x1
f=y3-y1
E=(e**2+f**2)**0.5
p=A+C+E
s=((p/2)*(p/2-A)*(p/2-C)*(p/2-E))**0.5
t=format( p,".4f" )
z=format( s,".4f" )
print(t,z)
