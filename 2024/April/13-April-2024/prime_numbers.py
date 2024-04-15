import time

def prime_number_1(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    #print(n, "is a prime number")
    return True

# Method Two
import math 


def prime_number_2(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            return False
    #print(n, "is a prime number")
    return True


# Method Three

def prime_number_3(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, math.isqrt(n)+1, 2):
        if n % i == 0:
            return False
    #print(n, "is a prime number")
    return True

to = time.time()
for n in range(1, 100000):
    prime_number_2(n)
t1 = time.time() 
print("Time taken by prime_number_1:", t1-to)