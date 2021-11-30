x1,y1,r1,x2,y2,r2=map(float,input().split())
a=(x2-x1)**2
b=(y2-y1)**2
if (x1==x2 and y1==y2 and r1==r2):
    print(-1)
elif (((a+b)**0.5)==r1+r2 or ((a+b)**0.5)==r1-r2 or ((a+b)**0.5)==r2-r1):
    print(1)
elif (((a+b)**0.5)>r1+r2 or ((a+b)**0.5)+r2<r1 or ((a+b)**0.5)+r1<r2):
    print(0)
else:
    print(2)
