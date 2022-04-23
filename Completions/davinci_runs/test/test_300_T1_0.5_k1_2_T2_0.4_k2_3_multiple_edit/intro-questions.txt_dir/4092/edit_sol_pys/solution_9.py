

def main():
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    prefix_sum_arr = [0] * (n + 1)

    for i in range(1, n + 1):
        prefix_sum_arr[i] = prefix_sum_arr[i-1] + arr[i]

    prefix_sum_dict = {}
    for i in range(n + 1):
        if prefix_sum_arr[i] in prefix_sum_dict:
            prefix_sum_dict[prefix_sum_arr[i]].append(i)
        else:
            prefix_sum_dict[prefix_sum_arr[i]] = [i]

    ans = 0
    for key in prefix_sum_dict:
        if len(prefix_sum_dict[key]) == 1:
            ans += 1
        else:
            ans += len(prefix_sum_dict[key]) - 1

    print(ans)

if __name__=="__main__":
    main()
