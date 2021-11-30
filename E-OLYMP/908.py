h=int(input())
n=list(map(int,input().split()))
k=0
s=0
for i in n:
    if i>0:
        if i%6==0:
            k=k+1
            s=s+i
print(k,int(s))
