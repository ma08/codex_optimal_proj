

    """
    This is a docstring. I have written it as a multiline comment.

    The task is to compute sum of two numbers N and M.
    """
def sum_even_ways(N, M):
    return N*M

N, M = [int(x) for x in input().split()]
print(sum_even_ways(N, M))
