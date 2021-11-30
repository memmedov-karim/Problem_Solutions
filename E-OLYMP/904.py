a=int(input())
n=list(map(int,input().split()))
for i in n:
    if i>=0:
        i=i+2
        print(i,end=" ")
    else:
        print(i,end=" ")
