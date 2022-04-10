

def main():
    n = int(input())
    s = input()
    t = input()

    s_idx = 0
    t_idx = 0
    swaps = 0
    swap_idxs = []

    while t_idx < n:
        if s[s_idx] == t[t_idx]:
            s_idx += 1
            t_idx += 1
        else:
            # swap
            swaps += 1
            swap_idxs.append(s_idx)
            s_idx += 2
            if s_idx > n:
                print(-1)
                return

    if swaps > 10000:
        print(-1)
        return

    print(swaps)
    print(' '.join(map(str, swap_idxs)))

if __name__ == '__main__':
    main()