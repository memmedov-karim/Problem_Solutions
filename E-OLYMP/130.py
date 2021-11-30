x1,y1,x2,y2,x3,y3=map(int,input().split())
for x4 in range(-100,101):
    for y4 in range(-100,101):
        if (x1-x2)**2+(y1-y2)**2==(x4-x3)**2+(y4-y3)**2 and (x4-x1)**2+(y4-y1)**2==(x3-x2)**2+(y3-y2)**2 and (x3-x1)**2+(y3-y1)**2==(x4-x2)**2+(y4-y2)**2:
            print(x4,y4)
