

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]
        a_count = {}
        for elem in a:
            a_count[elem] = a_count.get(elem, 0) + 1
        for elem in a:
            if a_count[elem] >= 3:
                print("YES")
                break
        else:
            print("NO")

if __name__ == '__main__':
    main()