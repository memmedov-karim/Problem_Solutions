denominations = [10, 20, 50, 100, 200, 500]
change=int(input())
A=[]
if change%10!=0:
    print(-1)
else:


    for pos, coin in enumerate(reversed(denominations)):

        while coin <= change:
            change = change - coin
            A.append(coin)
    print(len(A))
