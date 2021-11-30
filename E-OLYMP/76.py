a,b,x,y,z=map(int,input().split())
if a>x and b>y:
    print(1)
elif a>y and b>x:
    print(1)
elif a>x and b>z:
    print(1)
elif a>z and b>x:
    print(1)
elif a>y and b>z:
    print(1)
elif a>z and b>y:
    print(1)
else:
    print(0)
