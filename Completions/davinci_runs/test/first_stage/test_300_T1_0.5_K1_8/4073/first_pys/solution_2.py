

# Main
n = int(input())
a = [int(x) for x in input().split()]

# Solution
print(sum(a) - max(a))