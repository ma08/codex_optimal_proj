
#
# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
#
# def lcm(a, b):
#     return a * b // gcd(a, b)
#
# def main():
#     n = int(input())
#     nums = list(map(int, input().split()))
#     ret = 0
#     for i in range(n):
#         for j in range(i + 1, n):
#             ret = max(ret, (lcm(nums[i], nums[j]) - 1) % nums[i] + (lcm(nums[i], nums[j]) - 1) % nums[j])
#     print(ret)
#
# if __name__ == '__main__':
#     main()
