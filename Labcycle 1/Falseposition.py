def f(x):
    return x**3-4*x-9
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

def FalsePos(a,b,tol=1e-6,maxiter=100):
    iter=0
    while iter<maxiter:
        x = ((a*f(b))-(b*f(a)))/(f(b)-f(a))
        if abs(f(x))<tol:
            print("Root found:x=",x,"after ",iter," iterations")
            return x
        if f(x)==0:
            print("The root is:",x)
        if f(a)*f(x)<0:
            b=x
        else:
            a=x
        iter+=1
    print("Maximum iterations reached.Approximate root:x",x)
    return x

root=FalsePos(a,b)
print("The root is approximately:",root)

    