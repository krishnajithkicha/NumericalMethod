
import sympy as sp
def f(x):
    return x**3+2*x-2
def df(x):
    x_symbolic = sp.symbols('x')  # Symbolic variable
    f_symbolic = x_symbolic**3 + 2*x_symbolic - 2
    f_prime_symbolic = sp.diff(f_symbolic, x_symbolic)
    #print("Derivative of f(x):", f_prime_symbolic)
    derivative_value = f_prime_symbolic.subs(x_symbolic, x)
    return derivative_value
def interval():
    i=0
    while f(i)*f(i+1)>=0:
        if f(i)==0:
            print("The root is:",i)
            return i
        else:
            i+=1
    return i
a=interval()
b=a+1
print("The initial interval is:")
print("[",a,",",b,"]")

if abs(f(a))>=abs(f(b)):
    x=b
else:
    x=a
tolerance=1e-6
def NewtRaph(x):
    x0 = x
    while True:  
        derivative_value = float(df(x)) 
        if derivative_value == 0:  
            print("Derivative is zero, stopping iteration.")
            return x
        x1=x0-f(x0)/derivative_value
        if abs(x1 - x0) < tolerance:
            return x1
        x0= x1
        #print(x1)
val=NewtRaph(x)   
print("The root is:",val)

