

def main():
    n, k = [int(x) for x in input().split()]
    s = input()
    router_indices = [i for i, x in enumerate(s) if x == '1']
    router_indices.append(-1)
    router_indices.append(n)
    router_indices.sort()
    router_indices = [0] + router_indices
    i = 1
    ans = 0
    while i < len(router_indices):
        if router_indices[i] - router_indices[i - 1] - 1 <= k:
            i += 1
        else:
            ans += router_indices[i] - router_indices[i - 1]
            i += 2
    print(ans)

if __name__ == '__main__':
    main()