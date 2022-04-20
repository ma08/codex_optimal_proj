

counter = 0

def div2(n):
    if n % 2 == 0:
        return True
    else:
        return False

def div3(n):
    if n % 3 == 0:
        return True
    else:
        return False

def main():
    n = int(input())
    l = list(map(int, input().split()))
    global counter
    for i in range(n):
        if div2(l[i]):
            l[i] = l[i] // 2
            counter += 1
        elif div3(l[i]):
            l[i] = l[i] // 3
            counter += 1
    print(counter)

if __name__ == "__main__":
    main()