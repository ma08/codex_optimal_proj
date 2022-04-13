from collections import defaultdict

def sum_even_ways(N, M, K):
    if K == 0:
        return N*M
    elif K == 1:
        return N*M*2
    elif K == 2:
        return N*M*2
    elif K == 3:
        return N*M*2
    elif K == 4:
        return N*M*2
    elif K == 5:
        return N*M*2
    elif K == 6:
        return N*M*2
    elif K == 7:
        return N*M*2
    elif K == 8:
        return N*M*2
    elif K == 9:
        return N*M*2
    else:
        return N*M*2

N, M, K = [int(x) for x in input().split()]
print(sum_even_ways(N, M, K))
