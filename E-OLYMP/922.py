n=int(input())
n1=input().split()

c=[]
for i in range(n):
    c.append(n1[i-1])

for j in c:
    print(j, end=' ')
