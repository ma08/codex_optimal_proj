

import sys

def main():
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    assert(len(s) == n)
    assert(all(c in '012' for c in s))
    assert(n % 3 == 0)

    zeros = s.count('0')
    ones = s.count('1')
    twos = s.count('2')
    assert(zeros == ones == twos)

    # Replace one '1' with a '0' if the first character is '1'.
    if s[0] == '1':
        s = '0' + s[1:]
        ones -= 1
        zeros += 1

    # Replace one '2' with a '0' if the last character is '2'.
    if s[-1] == '2':
        s = s[:-1] + '0'
        twos -= 1
        zeros += 1

    # Replace one '1' with a '2' if the last character is '1'.
    if s[-1] == '1':
        s = s[:-1] + '2'
        ones -= 1
        twos += 1

    # Replace one '0' with a '1' if the first character is '0'.
    if s[0] == '0':
        s = '1' + s[1:]
        zeros -= 1
        ones += 1

    # Replace one '0' with a '2' if the last character is '0'.
    if s[-1] == '0':
        s = s[:-1] + '2'
        zeros -= 1
        twos += 1

    assert(zeros == ones == twos)
    assert(s[0] == '0')
    assert(s[-1] == '2')

    print(s)

if __name__ == "__main__":
    main()