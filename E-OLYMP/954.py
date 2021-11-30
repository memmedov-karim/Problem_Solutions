from math import sqrt
n=input().split()
a,b,h=float(n[0]),float(n[1]),float(n[2])
sahe=(a+b)*sqrt((a-b)*(a-b)+4*h*h)
print(format( sahe,".2f" ))
