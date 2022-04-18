
import sys

def main():
    passwords = []
    # get all the passwords
    for line in sys.stdin:
        passwords.append(line.strip().split())
    # convert to int and float
    passwords = [[int(p), float(prob)] for p, prob in passwords]
    # sort the passwords in decreasing order of probability
    passwords.sort(key=lambda x: x[1], reverse=True)
    # calculate the expected value
    expected = 0
    for i in range(len(passwords)):
        expected += (i + 1) * passwords[i][1]
    print(expected)

if __name__ == "__main__":
    main()
