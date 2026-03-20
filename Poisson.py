import math

lam=3
k=2

prob = math.exp(-lam)*(lam**k)/math.factorial(k)
print(prob)
