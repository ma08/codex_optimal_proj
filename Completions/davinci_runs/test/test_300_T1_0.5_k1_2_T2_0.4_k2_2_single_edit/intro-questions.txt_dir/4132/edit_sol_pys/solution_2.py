
# https://www.codechef.com/problems/KNIGHT


# My Solution
def get_min_moves(n, m, s, t):
    if n == 1 or m == 1:
        return 1
    if n == 2 or m == 2:
        return 2
    if n == 3 or m == 3:
        return 3
    if n == 4 or m == 4:
        return 4
    if n == 5 or m == 5:
        return 5
    if n == 6 or m == 6:
        return 6

n = int(input())
a = list(map(int, input().split()))

while len(a) > 1:
    a.sort()
    attacker = random.randint(0, len(a)-1)
    victim = random.randint(0, len(a)-1)
    if a[attacker] > a[victim]:
        a[victim] = 0
        a = [i for i in a if i != 0]
    else:
        a[attacker] = 0
        a = [i for i in a if i != 0]
print(a[0])
