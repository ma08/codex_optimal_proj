
def main():
    # input
    n = int(input())
    arr = list(map(int, input().split()))

    # processing
    prefix_sum = [0] * n
    for i in range(n):
        prefix_sum[i] = prefix_sum[i-1] + arr[i] if i > 0 else arr[i]

    prefix_sum_dict = {}
    for i in range(n):
        if prefix_sum[i] in prefix_sum_dict:
            prefix_sum_dict[prefix_sum[i]].append(i)
        else:
            prefix_sum_dict[prefix_sum[i]] = [i]

    ans = 0
    for key in prefix_sum_dict.keys():
        ans += len(prefix_sum_dict[key]) - 1

    print(ans)

    # output
    print(ans)

if __name__ == "__main__":
    main()
