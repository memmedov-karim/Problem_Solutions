x=int(input())
a=[]
a.append(1)
a.append(1)
for i in range(1,x-1):
    a.append(a[i]+a[i-1])
print(a[len(a)-1])
