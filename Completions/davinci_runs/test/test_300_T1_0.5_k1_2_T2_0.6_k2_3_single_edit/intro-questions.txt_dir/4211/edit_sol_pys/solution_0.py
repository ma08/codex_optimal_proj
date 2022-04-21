


def main():
    n = int(input())
    b = list(map(int, input().split()))
    a = []
    for i in range(n-1):
        if b[i] <= b[i+1]:
            a.append(b[i])
        else:
            a.append(b[i+1])
    a.append(b[n-2])
    print(sum(a))


if __name__ == '__main__':
    main()


# n = int(input())
# b = list(map(int, input().split()))
#
# a = []
#
# for i in range(n-1):
#     if b[i] <= b[i+1]:
#         a.append(b[i])
#     else:
#         a.append(b[i+1])
#
# a.append(b[n-2])
#
# print(sum(a))



n = int(input())
b = list(map(int, input().strip().split()))

if n == 2:
    print(b[0])
else:
    a = []
    for i in range(n-1):
        if b[i] <= b[i+1]:
            a.append(b[i])
        else:
            a.append(b[i+1])
    a.append(b[n-2])
    print(sum(a))
