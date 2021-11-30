a,b,c,d,f=map(float,input().split())
p1=(a+b+f)
p2=(c+d+f)
s1=((p1/2)*(p1/2-a)*(p1/2-b)*(p1/2-f))**0.5
s2=((p2/2)*(p2/2-c)*(p2/2-d)*(p2/2-f))**0.5
z=s1+s2
k=format( z,".4f" )
print(k)
