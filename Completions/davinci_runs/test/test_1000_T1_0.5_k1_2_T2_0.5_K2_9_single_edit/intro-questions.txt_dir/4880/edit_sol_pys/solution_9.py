

def main():
    with open("file.txt", "r") as f:
        n, m = map(int, f.readline().split())
        last = f.readline()
        cipher = f.readline()
        key = last + cipher[:m-n]
        plain = ""
        for i in range(m):
            plain += chr((ord(cipher[i]) - ord(key[i]) + 26) % 26 + ord('a'))
        print(plain)

main()
