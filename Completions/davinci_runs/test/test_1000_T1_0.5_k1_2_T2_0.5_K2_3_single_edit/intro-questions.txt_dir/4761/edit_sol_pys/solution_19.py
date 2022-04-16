

def main():
    low, high = [int(x) for x in input().split()]
    num_combinations = 0
    for i in range(low, high + 1):
        if is_valid(i):
            num_combinations += 1
    print(num_combinations)

def is_valid(n):
    n = str(n)
    if len(n) != 6:
        return False
    if len(set(n)) != 6:
        return False
    for i in n:
        if int(n) % int(i) != 0:
            return False
    return True

main()
