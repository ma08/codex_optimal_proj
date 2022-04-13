
import sys

def main():
    passwords = []
    for line in sys.stdin:
        passwords.append(line.strip().split())
    passwords = [[int(p), float(prob)] for p, prob in passwords if p != ' ']
    passwords.sort(key=lambda x: x[1], reverse=True)
    # print(passwords)
    expected = 0
    for i in range(len(passwords)):
        expected += (i + 1) * passwords[i][1]
    print(expected)

if __name__ == "__main__":
    main()
