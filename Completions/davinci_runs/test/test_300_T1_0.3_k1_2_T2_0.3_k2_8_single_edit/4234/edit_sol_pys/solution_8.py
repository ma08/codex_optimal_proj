

def main():
    n = int(input())  # number of elements in the set
    s = set(map(int, input().split()))  # set s
    N = int(input())  # number of other sets
    for i in range(N):
        command = input().split()
        if command[0] == "intersection_update":
            s.intersection_update(set(map(int, input().split())))
        elif command[0] == "update":
            s.update(set(map(int, input().split())))
        elif command[0] == "symmetric_difference_update":
            s.symmetric_difference_update(set(map(int, input().split())))
        elif command[0] == "difference_update":
            s.difference_update(set(map(int, input().split())))
    print(sum(s))

if __name__ == "__main__":
    main()
