

gunnar_first, gunnar_second, gunnar_third, gunnar_fourth = [int(x) for x in input().split()]  # [1, 2, 3, 4]
emma_first, emma_second, emma_third, emma_fourth = [int(x) for x in input().split()]  # [5, 6, 7, 8]

g = 0
e = 0

for i in range(gunnar_first, gunnar_second + 1):
    for j in range(gunnar_third, gunnar_fourth + 1):
        if i + j > emma_first + emma_second + emma_third + emma_fourth:
            g += 1
        elif i + j < emma_first + emma_second + emma_third + emma_fourth:
            e += 1

if g > e:
    print("Gunnar")
elif g < e:
    print("Emma")
else:
    print("Tie")
