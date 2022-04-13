
# ----- Solution 1 -----
#
# def main():
#     t = int(input())
#     for i in range(t):
#         n = int(input())
#         a = list(map(int, input().split()))
#         count = 0
#         for j in range(n):
#             if a[j] % 3 == 0:
#                 count += 1
#         for j in range(n):
#             for k in range(j+1, n):
#                 if (a[j]+a[k]) % 3 == 0:
#                     count += 1
#                     break
#         print(count)


# if __name__ == '__main__':
#     main()

# ----- Solution 2 -----
#
# def main():
#     t = int(input())
#     for i in range(t):
#         n = int(input())
#         a = list(map(int, input().split()))
#         a.sort()
#         count = 0
#         for j in range(n):
#             if a[j] % 3 == 0:
#                 count += 1
#         for j in range(n):
#             for k in range(j+1, n):
#                 if (a[j]+a[k]) % 3 == 0:
#                     count += 1
#                     break
#         print(count)
#
# if __name__ == '__main__':
#     main()

# ----- Solution 3 -----
#
def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        count = 0
        a.sort()
        for j in range(n-1):
            for k in range(j+1, n):
                if (a[j]+a[k]) % 3 == 0:
                    count += 1
                    break
        for j in range(n):
            if a[j] % 3 == 0:
                count += 1
        print(count)

if __name__ == '__main__':
    main()
