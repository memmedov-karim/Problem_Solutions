a,b,c=map(int,input().split())
d=b**2-4*a*c
x1=(-b+d**0.5)/(2*a)
x2=(-b-d**0.5)/(2*a)
if d<0:
    print("No roots")
elif d==0:
    print("One root:",int(x1))
elif d>0:
    if x2<x1:
        print("Two roots:",int(x2),int(x1))
    else:
        print("Two roots:",int(x1),int(x2))
