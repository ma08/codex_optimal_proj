

def main():
    L, H = map(int, input().split())
    count = 0
    for i in range(L, H + 1):
        if len(set(str(i))) == 6 and i % 2 != 0 and i % 5 != 0 and i % 3 != 0:
            count += 1
    print(count)

main()
