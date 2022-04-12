

def main():
    num = int(input())
    if num % 2 == 0:
        print("Alicia")
        print(num // 2 - 1)
    else:
        print(num // 2)
        print("Bob")

if __name__ == "__main__":
    main()
