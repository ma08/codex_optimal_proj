

def main():
    n, a = map(int, input().split())
    e = sorted(list(map(int, input().split())))[::-1]
    count = 0
    for i in e[::-1]:
        if a >= i:
            a -= i
            count += 1
        else:
            break
    print(count)

main()
