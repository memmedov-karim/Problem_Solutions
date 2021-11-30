n1=input().split()
x=float(n1[0])
y=float(n1[1])
if x>0 and y>0:
    print('1')
elif x<0 and y>0:
    print('2')
elif x<0 and y<0:
    print('3')
elif x==0 or y==0:
    print('0')
else:
    print('4')
