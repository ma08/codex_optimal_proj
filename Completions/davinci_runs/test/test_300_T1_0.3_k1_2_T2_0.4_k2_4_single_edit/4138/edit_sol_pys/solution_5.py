

def main():
    q = int(input())
    for i in range(q):
        k = int(input())
        print(get_digit(k))

def get_digit(k):
    num = 1
    while k > num:
        k -= num
        num += 1
    return str(num)[k-1]

if __name__ == "__main__":
    main()
