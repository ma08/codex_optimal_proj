n = int(input())
at_bats_list = list(map(int, input().split()))

official = 0
bases = 0
for i in at_bats_list:
    if i != -1:
        bases += i
        official += 1

print(bases / official)
