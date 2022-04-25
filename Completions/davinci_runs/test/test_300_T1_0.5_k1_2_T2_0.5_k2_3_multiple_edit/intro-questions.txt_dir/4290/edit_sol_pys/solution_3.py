def sum_even_ways(N, M, C):
    return N*M*C


N, M, C = [int(x) for x in raw_input().split()]
print(sum_even_ways(N, M, C))
