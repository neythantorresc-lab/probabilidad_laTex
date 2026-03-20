from scipy.stats import expon

prob = expon.cdf(2, scale=1)
print(prob)
