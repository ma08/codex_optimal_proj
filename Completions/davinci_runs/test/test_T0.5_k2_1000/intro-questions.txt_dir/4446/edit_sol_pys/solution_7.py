

n, a, b, k = map(int, input().split())
hp = list(map(int, input().split()))

hp.sort(reverse=True)

can_kill_in_one_turn = [True for _ in range(n)]
points = n
secret_technique_uses_left = k

for i in range(n):
    if hp[i] > a:
        can_kill_in_one_turn[i] = False
        if secret_technique_uses_left == 0:
            break
        secret_technique_uses_left -= 1
    if hp[i] > b:
        points -= 1

print(points)
