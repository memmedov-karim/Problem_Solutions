n=int(input())
a=int(n/1000)
b=n%1000
c=int(b/100)
d=n%100
e=int(d/10)
f=n%10
print((a+c+e+f)**2)
