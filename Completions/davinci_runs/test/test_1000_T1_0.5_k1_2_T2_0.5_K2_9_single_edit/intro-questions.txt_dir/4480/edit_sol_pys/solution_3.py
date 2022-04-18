import math



class Solution:
    def numOfSubarrays(self, arr, k, threshold):
        length = len(arr)
        if length < k:
            return 0
        sum_arr = [0 for _ in range(length)]
        sum_arr[0] = arr[0]
        for i in range(1, length):
            sum_arr[i] = sum_arr[i - 1] + arr[i]
        num = 0
        for i in range(k - 1, length):
            if i == k - 1:
                cur_sum = sum_arr[i]
            else:
                cur_sum = sum_arr[i] - sum_arr[i - k]
            if cur_sum / k >= threshold:
                num += 1
        return num


if __name__ == '__main__':
    arr = [2, 2, 2, 2, 5, 5, 5, 8]
    k = 3
    threshold = 4
    print(Solution().numOfSubarrays(arr, k, threshold))
