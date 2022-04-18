
def count_combinations(L, H):
    count = 0
    for c in range(L, H + 1):
        c_list = [int(d) for d in str(c)]
        if len(c_list) == len(set(c_list)) and all(
            [c % d == 0 for d in c_list]
        ):
            count += 1
    return count


def main():
    L, H = [int(x) for x in input().split()]
    print(count_combinations(L, H))


if __name__ == "__main__":
    main()
