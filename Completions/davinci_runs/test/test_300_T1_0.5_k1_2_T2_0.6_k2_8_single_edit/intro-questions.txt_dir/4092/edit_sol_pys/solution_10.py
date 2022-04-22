

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    prefix_sum = [0] * (n)

    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]

    prefix_sum_dict = {}
    for i in range(n):
        if prefix_sum[i] in prefix_sum_dict:
            prefix_sum_dict[prefix_sum[i]].append(i)
        else:
            prefix_sum_dict[prefix_sum[i]] = [i]

    ans = 0
    for key in prefix_sum_dict:
        if len(prefix_sum_dict[key]) == 1:
            ans += 1
        else:
            ans += len(prefix_sum_dict[key]) - 1

    print(ans)

if __name__=="__main__":
    main()
