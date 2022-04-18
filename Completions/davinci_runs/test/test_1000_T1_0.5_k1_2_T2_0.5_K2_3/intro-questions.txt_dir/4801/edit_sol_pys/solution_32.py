
# ---=== FUNCTIONS ===---
def get_input():
    """
    Gets and returns input from stdin.
    """
    n = int(input())
    a = [int(x) for x in input().split()]
    return n, a

def get_lis(a):
    """
    Returns the LIS of the given sequence.
    """
    n = len(a)
    lis = [a[0]]
    for i in range(1, n):
        if a[i] > lis[-1]:
            lis.append(a[i])
    return lis

def print_lis(lis):
    """
    Prints the given LIS.
    """
    print(len(lis))
    print(" ".join([str(x) for x in lis]), end="")

# ---=== MAIN ===---
n, a = get_input()
lis = get_lis(a)
print_lis(lis)
