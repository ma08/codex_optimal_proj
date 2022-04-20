

# SOLUTION
# This is a greedy problem.
# We can just play as many times as possible, and then play and charge as many times as possible
# until the end of the game.

# The first thing we need to do is figure out how many times we can just play.
# We can do this by dividing the initial charge by the charge used for just playing.
# The result is the number of times we can just play.
# We can then subtract this number from the total number of turns in the game.
# The result is the number of times we can play and charge.
# If the number of times we can play and charge is at least 1, then we can complete the game.
# Otherwise, we cannot.

# The second thing we need to do is figure out how many times we can play and charge.
# We can do this by dividing the initial charge by the charge used for playing and charging.
# The result is the number of times we can play and charge.

# The third thing we need to do is figure out how many times we can just play.
# We can do this by subtracting the number of times we can play and charge from the total number of turns.
# The result is the number of times we can just play.

# We can then print the number of times we can just play, or -1 if we cannot complete the game.

q = int(input())
for _ in range(q):
    k, n, a, b = map(int, input().split())
    if k < a and k < b:
        print(-1)
    else:
        print(k // a - min(k // a, n - k // b))