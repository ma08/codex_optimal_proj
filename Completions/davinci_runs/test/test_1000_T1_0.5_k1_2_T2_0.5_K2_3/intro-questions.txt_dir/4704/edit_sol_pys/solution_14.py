N = int(input())
cards = list(map(int, input().split()))

sum_cards = [0] * (N + 1)
for i in range(1, N + 1):
    sum_cards[i] = sum_cards[i - 1] + cards[i - 1]

min_diff = float('inf')
for i in range(1, N + 1):
    diff = abs(sum_cards[i] - (sum_cards[N] - sum_cards[i]))
    min_diff = min(min_diff, diff)

print(min_diff)
