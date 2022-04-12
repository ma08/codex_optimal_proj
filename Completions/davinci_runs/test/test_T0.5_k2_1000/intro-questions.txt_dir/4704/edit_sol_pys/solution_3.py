
N = int(input())
cards = list(map(int, input().split()))

sum_cards = [0] * (N + 1)
for i in range(N):
    sum_cards[i + 1] = sum_cards[i] + cards[i]

min_diff = float('inf')
for i in range(1, N):
    diff = abs(sum_cards[i] - (sum_cards[N] - sum_cards[i]))
    min_diff = min(min_diff, diff)

print(min_diff)
