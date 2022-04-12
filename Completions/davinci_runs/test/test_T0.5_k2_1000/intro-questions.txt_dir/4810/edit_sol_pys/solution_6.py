

def main():
    message = input()
    row = int(len(message) ** 0.5)
    col = int(len(message) / row) + 1
    for i in range(col):
        print(message[i::col], end="")

if __name__ == "__main__":
    main()
