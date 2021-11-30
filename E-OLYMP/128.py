n = int(input())
k = 0
for i6 in range(10):
    a6=i6
    for i5 in range(10):
        a5=i5
        for i4 in range(10):
            a4=i4
            for i3 in range(10):
                a3=i3
                for i2 in range(10):
                    a2=i2
                    for i1 in range(10):
                        a1=i1
                        if (a6+a5+a4) == (a3+a2+a1)and (a6+a5+a4) == n:
                            k+=1
print(k)
