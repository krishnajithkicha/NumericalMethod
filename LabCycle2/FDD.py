def f(x):
    return x**3+2*x**2-5*x+7

def FDD(x,h):
    fdd=(f(x+h)-f(x))/h
    return fdd
h=float(input("Enter the step size:"))
x=int(input("Enter the value of x:"))
f=FDD(x,h)
print("Forward Divided Difference value: ",f)