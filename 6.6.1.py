from math import sqrt, floor

#checking for prime numbers
#naive: check every value n-1
#less naive: check every value up to sqrt(x) 
# can we omit values? start at 2
# for i = 2 to range(sqrt(n)):
#   n / 2

n = int(input("Enter a number: "))

for i in range(2, int(sqrt(n)) + 1):
    if n % i == 0:
        print(f"{n} is not prime.") 
