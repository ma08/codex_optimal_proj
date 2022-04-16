

n = int(input())
s = input().split()

def get_count(s):
    count = 0
    for i in range(n):
        if s[i] == 'A':
            count += 4
        elif s[i] == 'B':
            count += 3
        elif s[i] == 'C':
            count += 2
        elif s[i] == 'D':
            count += 1
    return count

print(get_count(s))
