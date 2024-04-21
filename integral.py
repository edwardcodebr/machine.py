from scipy.integrate import quad
import math
def f(x):
    return x**2+2*x

intg, er = quad(f,0,1)
print("valor da integral", intg)
print("valor do erro", er)