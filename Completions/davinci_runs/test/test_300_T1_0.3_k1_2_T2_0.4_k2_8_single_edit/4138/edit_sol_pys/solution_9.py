
def main():
    q = int(input())
    for i in range(q):
        k = int(input())
        print(get_digit(k), end='')

def get_digit(k):
    n = 1
    while k > n:
        k -= n
        n += 1
    return str(n)[k-1]

if __name__ == "__main__":
    main()
