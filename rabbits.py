## Given: Positive integers n≤40 and k≤5

# Return: The total number of rabbit pairs that will be present after n  months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

# The population begins in the first month with a pair of newborn rabbits.
# Rabbits reach reproductive age after one month.
# In any given month, every rabbit of reproductive age mates with another rabbit of reproductive age.
# Exactly one month after two rabbits mate, they produce one male and one female rabbit.
# Rabbits never die or stop reproducing.

## Formula general fn = fn-1 + fn-2k


n = 5 # numero de meses
k = 3 # crias por generacion

def fib_k(k,n):
    if n == 1 or n == 2:
        #print(f"f{n} 1")
        return 1
    else:
        #print(f"f{n} {fib_k(k,n-1) + fib_k(k,n-2)*k}")
        return fib_k(k,n-1) + fib_k(k,n-2)*k

import time

#t0 = time.time()

#print(fib_k(1,40))

#t1 = time.time()

#print(t1-t0)

#######################################################################

## Programación dinámica

#memo = {"f1":1, "f2":1}


def dynfib_k(k, n, memo=None):
    if memo is None:
        memo = {1: 1, 2: 1}

    if n not in memo:
        memo[n] = dynfib_k(k, n-1, memo) + k * dynfib_k(k, n-2, memo)

    return memo[n]

T0 = time.time()

print(dynfib_k(4,29))

T1 = time.time()

print(T1-T0)

