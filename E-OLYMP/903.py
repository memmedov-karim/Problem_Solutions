n=int(input())
a=int(n/100)
b=n%10
k=max(a,b)
if a==b:
    print("=")
else:
    print(k)
