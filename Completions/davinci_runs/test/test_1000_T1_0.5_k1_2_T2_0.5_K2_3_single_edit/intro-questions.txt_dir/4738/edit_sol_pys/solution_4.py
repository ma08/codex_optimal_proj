

def main():
    s = input()
    for k in range(1, len(s) + 1):
        if s[:k] * (len(s) // k) == s:
            print(k)
            break

if __name__ == "__main__":
    main()
