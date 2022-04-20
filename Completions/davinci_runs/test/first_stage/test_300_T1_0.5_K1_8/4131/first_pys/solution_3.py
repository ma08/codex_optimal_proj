

# N: number of prefectures
# M: number of cities
# P_i: prefecture number of city i
# Y_i: year of establishment of city i
N, M = map(int, input().split())

# Dictionary to store the cities per prefecture
pref = {}
for i in range(M):
    P, Y = map(int, input().split())
    if P in pref:
        pref[P].append(Y)
    else:
        pref[P] = [Y]

# Sort the cities per prefecture
for i in pref:
    pref[i].sort()

# Print the result
for i in range(M):
    P, Y = map(int, input().split())
    print("{:06d}{:06d}".format(P, pref[P].index(Y) + 1))