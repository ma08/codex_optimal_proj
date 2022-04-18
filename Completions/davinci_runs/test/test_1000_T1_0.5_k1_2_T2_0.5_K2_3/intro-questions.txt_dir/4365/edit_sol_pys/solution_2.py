

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    k = int(input()) 
    result = 0

    for i in range(1, k + 1):
        if i % 2 == 0:
            result += 1

    print(result)
