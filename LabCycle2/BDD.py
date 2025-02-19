import math
def f(x):
    return math.exp(x)
def BDD(x,h):
    bdd=(f(x)-f(x-h))/h
    return bdd
h=float(input("Enter the step size:"))
x=int(input("Enter the value of x:"))
f=BDD(x,h)
print("Backward Divided Difference value: ",f)