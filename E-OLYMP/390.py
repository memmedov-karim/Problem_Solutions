from math import factorial
n=input()
v=set(n)
k=0
mass=[]
for i in v:
    k=n.count(i)
    mass.append(k)
rez=factorial(len(n))
for i in mass:
    rez/=factorial(i)
print(int(rez))
