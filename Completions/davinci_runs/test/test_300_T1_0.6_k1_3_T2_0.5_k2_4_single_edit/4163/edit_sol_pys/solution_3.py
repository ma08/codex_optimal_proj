

def main():
    n = int(input()) # read a line with a single integer
    doublets_count = 0
    for i in range(n):
        d1, d2 = map(int, input().split()) # read a list of integers, 2 in this case
        if d1 == d2:
            doublets_count += 1
        else:
            doublets_count = 0
        if doublets_count == 3:
            break
    if doublets_count == 3:
        print("Yes")
    else:
        print("No")
