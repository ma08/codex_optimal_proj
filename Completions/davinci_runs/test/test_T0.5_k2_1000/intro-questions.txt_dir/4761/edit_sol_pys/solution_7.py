

def main():
    l, h = map(int, input().split())
    count = 0
    for i in range(l, h + 1):
        if len(set(str(i))) == 6 and i % 2 != 0 and i % 5 != 0:
            if i % 1 == 0 and i % 3 == 0 and i % 4 == 0 and i % 6 == 0 and i % 7 == 0 and i % 8 == 0 and i % 9 == 0:
                count += 1
    print(count)

main()
