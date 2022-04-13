

N = int(input())

for i in range(N):
    a, b = map(int, input().split())

    if a * b % 2 == 0:
        print("Even")
    else:
        print("Odd")
