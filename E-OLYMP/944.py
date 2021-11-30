def SQ(x1,y1,z1,x2,y2,z2,x3,y3,z3):
    s=0.5*(((y2-y1)*(z3-z1)-(z2-z1)*(y3-y1))**2+((x2-x1)*(z3-z1)-(z2-z1)*(x3-x1))**2+((x2-x1)*(y3-y1)-(y2-y1)*(x3-x1))**2)**0.5
    return s
n=input().split()
xa,ya,za=int(n[0]),int(n[1]),int(n[2])
n=input().split()
xb,yb,zb=int(n[0]),int(n[1]),int(n[2])
n=input().split()
xc,yc,zc=int(n[0]),int(n[1]),int(n[2])
n=input().split()
xs,ys,zs=int(n[0]),int(n[1]),int(n[2])
s1=SQ(xa,ya,za,xb,yb,zb,xc,yc,zc)#ABC
s2=0.5*(((yb-ya)*(zs-za)-(zb-za)*(ys-ya))**2+((xb-xa)*(zs-za)-(zb-za)*(xs-xa))**2+((xb-xa)*(ys-ya)-(yb-ya)*(xs-xa))**2)**0.5
s3=s=0.5*(((yc-yb)*(zs-zb)-(zc-zb)*(ys-yb))**2+((xc-xb)*(zs-zb)-(zc-zb)*(xs-xb))**2+((xc-xb)*(ys-yb)-(yc-yb)*(xs-xb))**2)**0.5
s4=s=0.5*(((yc-ya)*(zs-za)-(zc-za)*(ys-ya))**2+((xc-xa)*(zs-za)-(zc-za)*(xs-xa))**2+((xc-xa)*(ys-ya)-(yc-ya)*(xs-xa))**2)**0.5
s=s1+s2+s3+s4
print('%.1f' %s)
