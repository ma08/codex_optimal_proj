

def sum_even_numbers(N, M, K):
    return N*M*K

N, M, K = [int(x) for x in input().split()]
print(sum_even_numbers(N, M, K))
