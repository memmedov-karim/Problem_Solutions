import math
n=input().split()
R=int(n[0])
r=int(n[1])
h=int(n[2])
s=math.pi*((h*h+(R-r)**2)**0.5)*(R+r)+math.pi*(R**2+r**2)
print(format( s,".2f" ))
