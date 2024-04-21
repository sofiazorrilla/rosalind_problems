## Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).

## Given: Positive integers n≤100  and m≤20.

# Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

import time

def dynfib_k(k = 1, n = 1, memo=None, m = 2):
    if memo is None:
        memo = {1: 1, 2: 1}

    if n not in memo:
        if n <= m: 
            memo[n] = dynfib_k(k, n-1, memo, m) + k * dynfib_k(k, n-2, memo, m)
        elif n == m+1:
            memo[n] = dynfib_k(k, m-1, memo, m) + dynfib_k(k, m, memo, m) - 1
        else:
            memo[n] = dynfib_k(k, n-2, memo, m) + dynfib_k(k, n-1, memo, m) - (dynfib_k(k, n-m-1, memo, m))

    #print(memo)
    return memo[n]

T0 = time.time()

print(dynfib_k(n = 81, m = 16))

T1 = time.time()

print(T1-T0)

## Mejor solucion del problema entre las soluciones publicadas

def fib(n=6,k=3):
  ages = [1] + [0]*(k-1)
  for i in range(n-1):
    ages = [sum(ages[1:])] + ages[:-1]
    print(ages)
  print(ages)
  return sum(ages)


T0 = time.time()

print(fib(n = 81, k = 16))

T1 = time.time()

print(T1-T0)