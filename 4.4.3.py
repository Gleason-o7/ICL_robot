#sqrt estimator?
# while(abs(n * n - val) >= 0.00001)
#   if (mul * n < val):
#       n *= mul
#   else:
#       mul /= 2

val = float(input("Enter a float (1.0, 9.333, 0.6311...):\n\t>> "))

n = 1.
mul = val / 2
epsilon = 0.00000001
while(abs(n * n - val) >= epsilon):
    if (n * n <= val):
        n += mul
    else:
        n -= mul
        mul /= 2

print(f"sqrt of {val} is {n}")

