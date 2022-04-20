

N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]

points = 0
for i in range(N-1):
    if A[i+1] - A[i] == 1:  # if the next card is same suit
        points += (B[A[i]-1] + C[A[i]-1])  # add the value of the card + the value of the card of the same suit
    else:
        points += B[A[i]-1]  # if the next card is not the same suit, add the value of the card
points += B[A[N-1]-1]  # add the value of the last card
print(points)
