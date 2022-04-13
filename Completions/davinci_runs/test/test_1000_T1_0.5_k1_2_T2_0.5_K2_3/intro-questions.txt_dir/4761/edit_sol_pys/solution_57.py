

def main():
    low, high = [int(x) for x in input().split()]
    num_permutations = 0
    for i in range(low, high + 1):
        if is_valid(i):
            num_permutations += 1
    print(num_permutations)

def is_valid(n):
    n = str(n)
    if len(n) != 6:
        return False
    if len(set(n)) != 6:
        return False
    for i in range(1, 10):
        if n.count(str(i)) > 1:
            return False
    for i in range(1, 10):
        if int(n) % i != 0:
            return False
    return True

main()
