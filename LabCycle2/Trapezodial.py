#Trapezoidal rule
def f(x):
  return (x**2)
def trapezoidal(a,b):
  h=(b-a)/n
  sum=f(a)+f(b)
  for i in range (1,n):
    sum+=2*(f(a+i*h))
  sum=sum*h/2
  return sum

a=int(input("Enter the lower limit: "))
b=int(input("Enter the upper limit: "))
n=int(input("Enter the n:"))
print("The integral is:",trapezoidal(a,b))
trapezoidal(a,b)