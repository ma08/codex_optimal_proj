def main():
    P, N = map(int, input().split())
    parts = []
    for i in range(N):
        part = input().strip()
        if part in parts:
            print(i + 1)
            return

        parts.append(part)
        if len(parts) == P:
            print(i + 1)
            return

    print("paradox avoided")

if __name__ == '__main__':
    main()
