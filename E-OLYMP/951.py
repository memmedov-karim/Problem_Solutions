n=int(input())
a=n%10
b=int((n%100)/10)
c=int((n%1000)/100)
d=int(n/1000)
print(1000*d+100*b+10*c+a)
