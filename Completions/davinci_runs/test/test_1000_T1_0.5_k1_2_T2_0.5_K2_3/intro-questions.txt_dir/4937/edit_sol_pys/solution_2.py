

def main():
    n, a = map(int, input().split())
    e = list(map(int, input().split()))
    count = 0
    for i in e[::-1]:
        if a >= i:
            a -= i
            count += 1
        else:
            break
    print(count)

main()
