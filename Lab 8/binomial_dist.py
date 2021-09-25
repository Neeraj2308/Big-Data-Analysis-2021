import math
def pbin(n,x,p):
    a=(math.comb(n,x))
    b=(p**(x))
    c=(1-p)**(n-x)
    d=a*b*c
    return(d)

print(pbin(20, 12, 0.5))

