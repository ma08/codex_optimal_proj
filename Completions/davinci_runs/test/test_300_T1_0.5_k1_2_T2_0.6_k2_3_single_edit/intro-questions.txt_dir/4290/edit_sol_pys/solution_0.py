

def sum_even_ways(N, M):
    return N*M % 1000000007

N, M = [int(x) for x in input().split()]
print(sum_even_ways(N, M))
