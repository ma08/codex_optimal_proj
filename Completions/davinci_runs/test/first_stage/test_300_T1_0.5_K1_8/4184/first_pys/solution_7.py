

N = int(input())
W = list(map(int, input().split()))

# S1 + S2 = sum(W)
# |S1 - S2| = |sum(W[:T+1]) - sum(W[T+1:])|
# |S1 - S2| = |sum(W[:T]) + W[T] - sum(W[T+1:])|
# |S1 - S2| = |sum(W[:T]) - sum(W[T+1:]) + W[T]|
# |S1 - S2| = |sum(W[:T]) - sum(W[T+1:])| + W[T]
# |S1 - S2| = |S1 - S2| + W[T]
# |S1 - S2| = W[T]

# |S1 - S2| = min(W[1:])
print(min(W[1:]))