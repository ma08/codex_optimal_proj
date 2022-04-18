

def main():
    num = int(input())
    if num % 2 == 0:
        print("Alice")
        print(num // 2)
    else:
        print(num // 2 + 1)
        print("Bob")

if __name__ == "__main__":
    main()
