

def count_combinations(l, h):
    count = 0
    for c in range(l, h + 1):
        c_list = [int(d) for d in str(c)]
        if len(c_list) == len(set(c_list)) and all([c % d == 0 for d in c_list]) and c_list[0] != 0:
            count += 1
    return count


def main():
    l, h = [int(x) for x in input().split()]
    print(count_combinations(l, h))


if __name__ == "__main__":
    main()
