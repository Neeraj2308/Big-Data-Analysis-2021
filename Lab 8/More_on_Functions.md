### More on Functions

#### Functions with multiple arguments


```python
def addtwo(x, y):
    return(x + y)

```


```python
addtwo(12, 13)
```




    25




```python
addtwo(12)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-3-b265bcf5143c> in <module>
    ----> 1 addtwo(12)
    

    TypeError: addtwo() missing 1 required positional argument: 'y'


### Defining function for binomial distribution
$$P(X = x)\, = \, ^nC_x\,p^x\,(1-p)^{n-x}$$


```python
#P(X = x) = nCx p^x (1-p)^(n-x)
# n! / (x! * (n - x)!)
import math

def pbin(x, n, p):
    ncx = math.factorial(n) / (math.factorial(x) * math.factorial(n - x))
    prob = ncx * (p**x) * ((1-p)**(n - x))
    return(prob)
```

#### Defining arguments with name


```python
pbin(x = 4, n = 7, p = 0.5)
```




    0.2734375



If arguments are given in the same order then not required to write variables' name. See example:


```python
pbin(4, 7, 0.5)
```




    0.2734375



Arguments are not required to be in the same order if given by name. See example: 


```python
pbin(n = 7, x = 4, p = 0.5)
```




    0.2734375


