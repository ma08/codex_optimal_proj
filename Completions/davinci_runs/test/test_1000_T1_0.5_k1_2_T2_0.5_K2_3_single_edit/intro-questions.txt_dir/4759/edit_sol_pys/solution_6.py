
n = int(input())
at_bats = list(map(int, input().split()))

official_at_bats = 0
bases = 0
for i in at_bats:
    if i != -1:
        bases += i
        official_at_bats += 1

print(bases / official_at_bats)
