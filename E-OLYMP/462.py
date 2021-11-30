n=int(input())
klavis=list(map(int,input().split()))
m=int(input())
mklavis=list(map(int,input().split()))
ans=[]
ans1=[]
ans2=[]
ans3=[]
for i in range(1,n+1):
    ans.append(mklavis.count(i))
for i in range(len(klavis)):
    ans1.append(klavis[i]-ans[i])
for j in ans1:
    if j<0:
        ans2.append("yes")
    else:
        ans2.append("no")
for x in ans2:
    print(x)
