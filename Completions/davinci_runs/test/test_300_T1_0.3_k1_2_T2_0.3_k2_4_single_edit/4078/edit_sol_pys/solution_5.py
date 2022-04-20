
#
# import sys
#
# def main():
#     n, m = map(int, sys.stdin.readline().split())
#     a = list(map(int, sys.stdin.readline().split()))
#     segments = []
#     for i in range(m):
#         l, r = map(int, sys.stdin.readline().split())
#         segments.append((l, r))
#     segments.sort(key=lambda x: x[1] - x[0])
#     ans = 0
#     for i in range(m):
#         l, r = segments[i]
#         if a[l - 1] > a[r - 1]:
#             a[l - 1], a[r - 1] = a[r - 1], a[l - 1]
#         ans = max(ans, a[l - 1] - a[r - 1])
#     print(ans)
#     print(0)
#
# if __name__ == '__main__':
#     main()
