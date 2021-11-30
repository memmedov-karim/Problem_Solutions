n=int(input())
a=list(map(float,input().split()))
say=0
cem=0
for i in range(n):
    if a[i]<0:
        cem=cem+a[i]
        say+=1
print(say,end=' ')
print('%.2f'%cem)
