

# -*- coding: utf-8 -*- 

# AtCoder Beginner Contest 
# Problem B 

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    count = 0

    for i in range(N):
        while A[i] % 2 == 0:
            A[i] = A[i] // 2
            count += 1

    print(count)
