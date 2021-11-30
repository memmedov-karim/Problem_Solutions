m,n,k=map(int,input().split())
c=m//n
b=''
for i in range(k-1):
    m=((m%n)*10)
    b+=str(int(m/n))
m=(m%n)*10
a=int(m/n)
print(str(c)+'.'+b+str(a))
