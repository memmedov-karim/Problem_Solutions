n=int(input())
a=[]
for i in range(1,n+1):
    x=int(input())
    if (2*x)%6==2:
        a.append("VGC")
    elif (2*x)%6==4:
        a.append("CVG")
    elif (2*x)%6==0:
        a.append("GCV")
for i in a:
    print(i)
