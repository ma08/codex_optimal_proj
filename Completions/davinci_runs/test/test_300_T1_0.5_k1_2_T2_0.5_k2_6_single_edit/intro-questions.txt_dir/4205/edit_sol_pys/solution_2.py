

N = int(input())
sequence = list(map(int, input().split()))

print("YES") if sequence == sorted(sequence) else print("NO")
