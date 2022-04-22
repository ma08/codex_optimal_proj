

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr = [0] + arr
    prefix_sum = [0] * (n + 1)

    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]

    prefix_sum_dict = {}
    for i in range(n + 1):
        if prefix_sum[i] in prefix_sum_dict:
            prefix_sum_dict[prefix_sum[i]].append(i)
        else:
            prefix_sum_dict[prefix_sum[i]] = [i]

    ans = 0
    for key in prefix_sum_dict.keys():
        if len(prefix_sum_dict[key]) == 1:
            ans += 1
        else:
            ans += len(prefix_sum_dict[key]) - 1

    print(ans)


def main1():
    n = int(input())
    arr = list(map(int, input().split()))
    arr = [0] + arr
    prefix_sum = [0] * (n + 1)
    ans = 0

    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]

        if prefix_sum[i] in prefix_sum[:i]:
            ans += 1

            ans += len(prefix_sum_dict[key]) - 1

    print(ans)

if __name__=="__main__":
    main1()
