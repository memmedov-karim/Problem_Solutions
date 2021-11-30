def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
q=input().split()
m,n=int(q[0]),int(q[1])
g=gcd(m,n)

m /= g
n /= g
print(int(n + m - 2), end=' ')
if(n % 2 == 0 and m % 2 != 0):
    print(4)
elif (n % 2 != 0 and m % 2 != 0):
    print(3)
elif (n % 2 != 0 and m % 2 == 0):
    print(2)
