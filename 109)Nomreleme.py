def f(n):
    m=0
    for i in range(1,1000000):
        m+=len(str(i))
        if n==m:
            return i
    return 0
print(f(int(input())))
