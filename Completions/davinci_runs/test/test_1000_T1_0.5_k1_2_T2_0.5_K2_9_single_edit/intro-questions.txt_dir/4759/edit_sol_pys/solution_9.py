
n = int(input())
at_bats = list(map(int, input().split()))
print(sum(at_bats) / len([i for i in at_bats if i != -1]))
