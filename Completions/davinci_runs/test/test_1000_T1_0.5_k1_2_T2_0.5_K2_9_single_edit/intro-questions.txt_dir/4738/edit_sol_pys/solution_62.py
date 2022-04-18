

def main():
    s = input()
    k = 1
    while k <= len(s) // 2:
        if s[:k] * (len(s) // k) == s and len(s) % k == 0:
            print(k)
            break
        k += 1

if __name__ == "__main__":
    main()
