x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
x4,y4=map(int,input().split())
x=(x1+x3)/2
y=(y1+y3)/2
a=(x3-x1)**2
b=(y3-y1)**2
c=(x4-x2)**2
d=(y4-y2)**2
ab=(a+b)**0.5
cd=(c+d)**0.5
abf=format( ab,".3f" )
cdf=format( cd,".3f" )
xa=format( x,".3f" )
ya=format( y,".3f" )
print(xa,ya)
print(abf,cdf)
