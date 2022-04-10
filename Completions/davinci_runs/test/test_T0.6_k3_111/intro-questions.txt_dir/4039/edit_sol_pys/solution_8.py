
# test
import sys

def main():
    n, r = map(int, input().split())
    queue = []
    for i in range(n):
        a, b = map(int, input().split())
        queue.append((a, b))

    queue.sort(key=lambda x: x[0])
    queue.sort(key=lambda x: x[1])
    #print(queue)
    for a,b in queue:
        if r >= a:
            r += b
        else:
            print("NO")
            sys.exit(0)
    print("YES")

if __name__ == "__main__":
    main()
