

def sum_even_ways(N, M, P):
    return N*M*P

N, M, P = [int(x) for x in input().split()]
print(sum_even_ways(N, M, P))
