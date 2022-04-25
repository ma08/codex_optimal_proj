

def min_len(n, words, count):
    for i in range(n):
        if words[i] == words[i+1]:
            count += 1
            print("count", count)
        else:
            return count
            print("return", count)

n = int(input())
words = input().split()

print(min_len(n, words, count=1))
