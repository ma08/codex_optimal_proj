n = int(input())
days = [int(x) for x in input().split()]

cleanup = 0
dirtiness = 0

for day in days:
    dirtiness += day
    if dirtiness >= 20:
        cleanup += 1
        dirtiness = 0

print(cleanup)


# n = int(input())
# days = [int(x) for x in input().split()]

# cleanup = 0
# dirtiness = 0

# for day in days:
#     dirtiness += day
#     if dirtiness >= 20:
#         cleanup += 1
#         dirtiness = 0

# print(cleanup)
