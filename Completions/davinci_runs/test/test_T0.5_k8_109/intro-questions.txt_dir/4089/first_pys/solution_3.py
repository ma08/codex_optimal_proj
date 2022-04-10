

N = int(input())

# 1 <= N <= 26
if N <= 26:
    print(chr(ord('a') + N - 1))
    exit()

# 27 <= N <= 702
if N <= 702:
    print(chr(ord('a') + (N - 1) // 26 - 1) + chr(ord('a') + (N - 1) % 26))
    exit()

# 703 <= N <= 18278
if N <= 18278:
    print(chr(ord('a') + (N - 1) // 676 - 1) + chr(ord('a') + (N - 1) % 676 // 26) + chr(ord('a') + (N - 1) % 26))
    exit()

# 18279 <= N <= 475254
if N <= 475254:
    print(chr(ord('a') + (N - 1) // 17576 - 1) + chr(ord('a') + (N - 1) % 17576 // 676) + chr(ord('a') + (N - 1) % 676 // 26) + chr(ord('a') + (N - 1) % 26))
    exit()

# 475255 <= N <= 1000000000000001
print(chr(ord('a') + (N - 1) // 60466176 - 1) + chr(ord('a') + (N - 1) % 60466176 // 17576) + chr(ord('a') + (N - 1) % 17576 // 676) + chr(ord('a') + (N - 1) % 676 // 26) + chr(ord('a') + (N - 1) % 26))