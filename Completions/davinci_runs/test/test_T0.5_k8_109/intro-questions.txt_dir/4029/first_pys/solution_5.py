

def main():
    n = int(input())
    count = 0
    while n % 25 != 0:
        if n < 10:
            return -1
        n = str(n)
        for i in range(1, len(n)):
            if int(n[i]) < int(n[i-1]):
                n = n[:i-1] + n[i] + n[i-1] + n[i+1:]
                count += 1
                break
        n = int(n)
    return count

if __name__ == "__main__":
    print(main())