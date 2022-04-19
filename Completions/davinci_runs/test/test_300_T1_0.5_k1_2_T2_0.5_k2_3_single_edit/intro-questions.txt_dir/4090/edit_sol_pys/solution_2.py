
def min_length(n, words) -> int:
    count = 0
    for i in range(n):
        if words[i] not in words[i + 1:]:
            count += 1
    return n - count

n = int(input())
words = input().split()

print(min_length(n, words))
