

def main():
    message = input()
    row = int(len(message) ** 0.5)
    c = int(len(message) / row)
    for i in range(c):
        print(message[i::c], end="")

if __name__ == "__main__":
    main()
