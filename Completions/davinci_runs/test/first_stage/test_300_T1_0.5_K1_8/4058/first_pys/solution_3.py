

n, r = map(int, input().split())
a = list(map(int, input().split()))

# print(n, r, a)

def get_heaters(n, r, a):
    heaters = []
    for i in range(n):
        if a[i] == 1:
            heaters.append((i + 1, i + 1))
    return heaters

def check_heaters(n, r, a, heaters):
    for i in range(n):
        if a[i] == 0:
            covered = False
            for j in range(len(heaters)):
                if heaters[j][0] <= i + 1 <= heaters[j][1]:
                    covered = True
                    break
            if not covered:
                return False
    return True

def heat_up(n, r, a, heaters):
    for i in range(n):
        if a[i] == 0:
            covered = False
            for j in range(len(heaters)):
                if heaters[j][0] <= i + 1 <= heaters[j][1]:
                    covered = True
                    break
            if not covered:
                # print(i + 1, heaters)
                for j in range(len(heaters)):
                    if heaters[j][0] > i + 1:
                        heaters[j] = (i + 1, heaters[j][1])
                        break
                    if heaters[j][1] < i + 1:
                        heaters[j] = (heaters[j][0], i + 1)
                        break
                # print(i + 1, heaters)
    return heaters

def count_heaters(heaters):
    return len(heaters)

heaters = get_heaters(n, r, a)

# print(heaters)

if check_heaters(n, r, a, heaters):
    print(count_heaters(heaters))
else:
    heaters = heat_up(n, r, a, heaters)
    # print(heaters)
    if check_heaters(n, r, a, heaters):
        print(count_heaters(heaters))
    else:
        print(-1)