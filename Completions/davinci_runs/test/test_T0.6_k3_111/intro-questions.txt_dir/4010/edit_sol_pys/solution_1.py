

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [int(x) for x in input().split()][:n]
        a_counts = {}
        for elem in a:
            a_counts[elem] = a_counts.get(elem, 0) + 1  # a_counts[elem] = a_counts.get(elem, 0) + 1
        for elem in a:
            if a_counts[elem] >= 3:  # if a_counts[elem] >= 3:
                print("YES")
                break
        else:
            print("NO")

if __name__ == '__main__':
    main()
