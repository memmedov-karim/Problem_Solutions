t=int(input())
import math
answer=[]
for i in range(t):
    n,k=map(int,input().split())
    answer.append(int(math.comb(n,k)))
for i in answer:
    print(i)
