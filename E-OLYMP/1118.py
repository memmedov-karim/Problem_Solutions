n=int(input())
if n==0:
    print("Ooops!")
else:
    a=list(map(int,input().split()))
    if n==1:
        print("Ooops!")
    else:
        mn=a[0]
        for i in range(n):
            if a[i]<mn:
                mn=a[i]

        mk=a[0]
        for i in range(n):
            if a[i]>mk:
                mk=a[i]
        print(mn,mk)
