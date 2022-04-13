
# ----- Solution 2 -----
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

#!/usr/bin/python3

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        count = 0
        for j in range(n):
            if a[j] % 3 == 0:
                count += 1
        for j in range(n):
            for k in range(j+1, n):
                if (a[j]+a[k]) % 3 == 0:
                    count += 1
                    break
        print(count)

if __name__ == '__main__':
    main()
