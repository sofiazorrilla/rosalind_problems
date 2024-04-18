## Three positive integers k, m, and n, representing a population containing k+m+n  organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

## return the probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

input = [2,2,2]

k = input[0] # homocigotos dominantes
n = input[1] # heterocigotos
m = input[2] # homocigotos recesivos
T = k+n+m

def p_dominante(k,n,m):
    T = k+n+m
    return ((1-(m*(m-1)+m*n+n*(n-1)*0.25)/(T*(T-1))))

print(p_dominante(22,24,23))
print(p_dominante(24,17,19))