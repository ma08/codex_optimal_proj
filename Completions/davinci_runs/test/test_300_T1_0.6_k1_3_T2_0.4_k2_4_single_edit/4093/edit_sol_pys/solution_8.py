import sys

# def add_num(arr, num):
#     if not arr:
#         arr.append(num)
#         return arr
#     if num == 0:
#         arr.append(num)
#         return arr
#     if num < arr[-1]:
#         arr.append(num)
#         return arr
#     for i in range(len(arr)):
#         if arr[i] == 0:
#             arr[i] = num
#             return arr
#         if arr[i] > num:
#             arr[i] = num
#             return arr
#     arr.append(num)
#     return arr

# def main():
#     t = int(input())
#     for _ in range(t):
#         n, m = list(map(int, input().split()))
#         arr = []
#         while m > 0:
#             if m > n-1:
#                 arr = add_num(arr, n-1)
#                 m -= n-1
#             else:
#                 arr = add_num(arr, m)
#                 break
#         print(sum([abs(arr[i+1] - arr[i]) for i in range(len(arr)-1)]))

def main():
    # t = int(input())
    # for _ in range(t):
    #     n, m = list(map(int, input().split()))
    #     arr = [1]*(n-1)
    #     if m > n-1:
    #         arr.append(m - (n-1))
    #     else:
    #         arr[-1] = m
    #     print(sum([abs(arr[i+1] - arr[i]) for i in range(len(arr)-1)]))
    for line in sys.stdin:
        print(line)


if __name__ == "__main__":
    main()
