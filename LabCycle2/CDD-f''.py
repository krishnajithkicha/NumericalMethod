import math
def f(x):
    return math.sin(x)
def CDD(x,h):
    cdd=(f(x+h)+f(x-h)-(2*f(x)))/(h**2)
    return cdd
h=float(input("Enter the step size:"))
x=math.pi/4
f=CDD(x,h)
print("Second Derivative of Central Divided Difference value: ",f)