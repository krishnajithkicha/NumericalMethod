#newton's interpolation
import math
def forward(x, y, n,p):
  a=[]
  a.append(y)
  for i in range(n-1):
    b=[]
    for j in range(n-i-1):
      b.append(a[i][j+1]-a[i][j])
    a.append(b)


  u=(p-x[0])/(x[1]-x[0]) # u=x-x0/h

  sol=a[0][0]
  u_term=1
  for i in range(1,n):
    u_term*=(u-(i-1))
    sol+=(u_term*a[i][0])/math.factorial(i)
  print("The value of f(x) at point ",p," is:", sol)



  
n=int(input("Enter the number of values:"))
x=[]
for i in range(n):
  x.append(float(input("Enter the value of x:")))
y=[]
for i in range(n):
  y.append(float(input("Enter the value of y:")))
p=float(input("Enter the point:"))
forward(x, y, n, p)
