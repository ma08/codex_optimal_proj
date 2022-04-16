

n = int(input())
at_bats = list(map(int, input().split()))
# n = 3
# at_bats = [3, 0, 2]

total_bases = 0
total_at_bats = 0

for at_bat in at_bats:
    if at_bat != -1:
        total_bases += at_bat
        total_at_bats += 1

print(total_bases / total_at_bats)  # 3.0
