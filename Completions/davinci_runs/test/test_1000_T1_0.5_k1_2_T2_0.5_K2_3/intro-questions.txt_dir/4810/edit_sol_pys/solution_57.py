

def main():
    message = input()
    r = int(len(message) ** .5) + 1
    c = len(message) // r
    for i in range(c):
        print(message[i::c], end="")

if __name__ == "__main__":
    main()
