
n, a, b, k = map(int, input().split())
hp = list(map(int, input().split()))

# We will use a greedy approach to solve this problem.
# We want to use our secret technique as many times as possible.
# We also want to use our secret technique on the monsters with the lowest health points.
# This is because we want to use our secret technique on monsters that we can't kill in one turn.
# If we use our secret technique on a monster with high health points,
# we will run out of secret technique uses before we can use it on a monster with low health points.
# This is why we sort the monsters by their health points in descending order. 
hp.sort(reverse=True)

# We will use a list to keep track of which monsters we can kill in one turn.
# If we can kill a monster in one turn, we don't need to use our secret technique on it.
# If we can't kill a monster in one turn, we will use our secret technique on it.
# We start by assuming that we can kill every monster in one turn.
# If we later find out that we can't kill a monster in one turn, we will change the corresponding value in this list to False.
# We will also keep track of the number of points we will get from killing monsters.
# We start by assuming that we will get a point for killing every monster.
# If we later find out that we won't get a point for killing a monster, we will decrease the value in this list by one.
# We will also keep track of the number of secret technique uses we have left.
can_kill_in_one_turn = [True for _ in range(n)]
points = n
secret_technique_uses_left = k

# We will now loop through the monsters.
# We will check if we can kill the monster in one turn.
# If we can't, we will use our secret technique on it.
# If we can, we will check if our opponent can kill the monster in one turn.
# If he can, we will not get a point for killing the monster.
# If he can't, we will get a point for killing the monster.
for i in range(n):
    if hp[i] > a:
        can_kill_in_one_turn[i] = False
        if secret_technique_uses_left == 0:
            break
        secret_technique_uses_left -= 1
    if hp[i] > b:
        points -= 1

print(points)
