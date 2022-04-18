
# import sys

# def main():
#     K = int(sys.stdin.readline().strip())
#     desks = [int(sys.stdin.readline().strip()) for _ in range(K)]
#     desks.sort()
#     count = 0
#     for i in range(K):
#         count += 1
#         if desks[i] < i+1:
#             count += i - desks[i]
#     print(count)

# main()

def get_sum(n):
    if n == 1:
        return 1
    return n + get_sum(n-1)

print(get_sum(100))
