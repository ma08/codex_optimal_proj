
# SOLUTION
n = int(input())
s = input()


def is_possible(s, n, flag):
    color = [0] * n
    for i in range(n - 1):
        if s[i] > s[i+1]:
            flag = True
            break
    if flag:
        for i in range(n):
            if i % 2 == 0:
                color[i] = 1
            else:
                color[i] = 0
    else:
        for i in range(n):
            if i % 2 == 0:
                color[i] = 0
            else:
                color[i] = 1
    print("YES")
    print("".join(map(str,color)))


flag = False
is_possible(s, n, flag)
