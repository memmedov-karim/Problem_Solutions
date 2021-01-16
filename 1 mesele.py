x,y=map(float,input().split())
a=((x-y)**2)/(x**2+y**2-1)**0.5
b=((x**2+y**2-1)**0.5)/(2*x*y)
print(format( (b+a),".3f" ))
