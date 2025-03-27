#lagrange interpolation
import math
def lagrange(x, y, n,p):
  sol=0.0
  for i in range(n):
    num=1.0
    den=1.0
    for j in range(n):
      if i!=j: 
        num*=(p-x[j])
        den*=(x[i]-x[j]) # prevent division by zero
    sol+=(num/den)*y[i]
  print("The value of f(x) at point ",p," is:", sol)



  
n=int(input("Enter the number of values:"))
x=[]
for i in range(n):
  x.append(float(input("Enter the value of x:")))
y=[]
for i in range(n):
  y.append(float(input("Enter the value of y:")))
p=float(input("Enter the point:"))
lagrange(x, y, n, p)
