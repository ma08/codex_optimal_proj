

def sum_even_ways(N, M, A):
    return N*M*A

N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
print(sum_even_ways(N, M, A))
