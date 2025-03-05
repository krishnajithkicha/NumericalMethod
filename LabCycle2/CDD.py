import math
def f(x):
    return math.sin(x)
def CDD(x,h):
    cdd=(f(x+h)-f(x-h))/(2*h)
    return cdd
h=float(input("Enter the step size:"))
x=math.pi/4
f=CDD(x,h)
print("Central Divided Difference value: ",f)