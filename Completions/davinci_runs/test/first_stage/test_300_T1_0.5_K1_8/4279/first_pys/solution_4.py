

def main():
    q = int(input())
    for i in range(q):
        k = int(input())
        print(get_digit(k))

def get_digit(k):
    if k == 1:
        return 1
    total = 1
    i = 1
    while total < k:
        i += 1
        total += i
    total -= i
    diff = k - total
    num = i - diff + 1
    return int(str(num)[-1])

if __name__ == "__main__":
    main()