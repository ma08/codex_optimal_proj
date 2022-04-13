

def main():
    message = input()
    r = int(len(message) ** 0.5)
    c = int(len(message) / r)
    for i in range(c):
        print(message[i::c], end="")

if __name__ == "__main__":
    main()
