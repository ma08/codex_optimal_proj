

# -*- coding: utf-8 -*-

# AtCoder Regular Contest
# Problem A

if __name__ == '__main__':
    k = int(input())
    result = 1

    for i in range(1, k + 1):
        result *= i

    print(result)
