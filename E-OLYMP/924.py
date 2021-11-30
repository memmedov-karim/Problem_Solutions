import math
s,R1=map(float,input().split())
k=math.pi
R2=(R1**2-(s/k))**0.5
z=format( R2,".2f")
print(z)
