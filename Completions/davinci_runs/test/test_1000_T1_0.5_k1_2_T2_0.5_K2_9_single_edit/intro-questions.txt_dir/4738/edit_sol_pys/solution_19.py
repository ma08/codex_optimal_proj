

def main():
    s = input()
    length = len(s)
    for i in range(1, length):
        if length % i == 0:
            k = length // i
            if s[:i] * k == s:
                print(i)
                break

if __name__ == "__main__":
    main()
