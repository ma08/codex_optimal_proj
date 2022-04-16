

def main():
    n, a = map(int, input().split())  # n is number of elements and a is the target
    e = list(map(int, input().split()))  # list of elements
    e.sort()  # sorting the list
    count = 0
    for i in range(n):
        if a >= e[i]:
            a -= e[i]
            count += 1
        else:
            break
    print(count)

main()
