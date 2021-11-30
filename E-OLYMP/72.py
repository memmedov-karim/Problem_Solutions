n, k, t, v=map(int,input().split())
hx,hy=map(int,input().split())
x=0
y=0
for i in range(k+1):
    if i%4==0:
        x+=1+n*i
        y+=1+n*i
    elif i%4==1:
        x+=1+n*i
        y-=1+n*i
    elif i%4==2:
        x-=1+n*i
        y-=1+n*i
    elif i%4==3:
        x-=1+n*i
        y+=1+n*i

if (t*t*v*v*2>=(x-hx)*(x-hx)+(y-hy)*(y-hy)):
    print( "Good night Ia")
else:
    print( "Poor Ia")
