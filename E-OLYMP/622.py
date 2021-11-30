n=int(input())
a=""
while n!=0:
    a=a+str(n%2)
    n=int(n/2)
print(a.count("1"))
