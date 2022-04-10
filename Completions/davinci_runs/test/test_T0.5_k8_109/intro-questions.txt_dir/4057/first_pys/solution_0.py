

n = int(input())
a = [int(i) for i in input().split()]

def find_min_pockets(a):
    a.sort()
    curr_pockets = 1
    curr_pocket = [a[0]]
    for i in range(1, len(a)):
        if a[i] in curr_pocket:
            curr_pocket = [a[i]]
            curr_pockets += 1
        else:
            curr_pocket.append(a[i])
    return curr_pockets

print(find_min_pockets(a))