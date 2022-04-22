

def prefix_sum(arr):
    n = len(arr)
    prefix_sum_dict = {}
    for i in range(n):
        if prefix_sum[i] in prefix_sum_dict:
            prefix_sum_dict[prefix_sum[i]].append(i)
        else:
            prefix_sum_dict[prefix_sum[i]] = [i]

    return prefix_sum_dict

def count_ans(prefix_sum_dict):
    ans = 0
    for key in prefix_sum_dict:
        if len(prefix_sum_dict[key]) == 1:
            ans += 1
        else:
            ans += len(prefix_sum_dict[key]) - 1
    return ans

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr = [0] + arr
    prefix_sum = [0] * (n + 1)

    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]

    prefix_sum_dict = prefix_sum(prefix_sum)
    print(count_ans(prefix_sum_dict))
    
if __name__=="__main__":
    main()
