def f(x):
    return 2/(1+x**3)


def simpsons(a,b,h):
    evensum=0
    oddsum=0
    for i in range(1,n):
        if(i%2==0):
            evensum=evensum+f(a+i*h)
        else:
            oddsum=oddsum+f(a+i*h)
    simps=(h/3)*(f(a)+f(b)+4*oddsum+2*evensum)
    return simps
a=float(input("Enter the lower limit:"))
b=float(input("Enter the upper limit:"))
n=int(input("Enter the number of iterations:"))
h=(b-a)/n
s=simpsons(a,b,h)
print("Value of Intergral using Simpsons 1/3rd rule:",s)