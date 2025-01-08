def f(x):
    return x**2-4

def bisection_method(a, b, tol, max_iter):
    # Check if the function changes signs over the interval
    if f(a)*f(b)>=0:
        print("Function does not change signs over the interval. Please choose different a and b.")
        return None   
    iteration = 0
    while iteration < max_iter:
        #midpoint of the interval
        c = (a + b) / 2   
        # Checking if the result is within tolerance
        if abs(f(c)) < tol: 
            return c
        # If f(c) is of opposite sign to f(a), move the end point to c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c        
        iteration += 1    
    print("Maximum iterations reached",max_iter,"Approximate root:",c)
    return c

# Input interval [a, b]
a = float(input("Enter the start of the interval (a): "))
b = float(input("Enter the end of the interval (b): "))

# Tolerance and max iterations
tol=1e-6 #10^-6
max_iter = int(input("Enter the maximum number of iterations: "))

root = bisection_method(a, b, tol, max_iter)
if root is not None:
    print("The root is approximately:",root)
