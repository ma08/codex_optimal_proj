
import sys

def main():
    passwords = []
    for line in sys.stdin:
        passwords.append(line.strip().split())
    passwords = [[int(p), float(prob)] for p, prob in passwords]
    passwords.sort(key=lambda x: x[1], reverse=True)
    expected = 0
    for i in range(len(passwords)):
        expected += (i + 1) * passwords[i][1] * passwords[i][0]
    print(expected)

if __name__ == "__main__":
    main()
