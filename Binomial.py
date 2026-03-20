from math import comb

n=5
p=0.5
k=3

prob = comb(n,k)*(p**k)*((1-p)**(n-k))
print(prob)
