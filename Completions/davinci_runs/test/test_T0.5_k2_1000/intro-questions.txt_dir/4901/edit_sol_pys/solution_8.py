import sys

def main():
    message = sys.stdin.readline().strip()
    half1 = message[:len(message) // 2]
    half2 = message[len(message) // 2:]
    rotate1 = rotate(half1)
    rotate2 = rotate(half2)
    merge = merge(rotate1, rotate2)

    print(merge)

def rotate(s):
    rotate_num = 0
    for i in range(len(s)):
        rotate_num += ord(s[i]) - ord('A')
    rotate_num = rotate_num % 26
    rotate_message = ''
    for i in range(len(s)):
        rotate_message += chr((ord(s[i]) - ord('A') + rotate_num) % 26 + ord('A'))
    return rotate_message


def merge(s1, s2):
    merge_message = ''
    for i in range(len(s1)):
        merge_message += chr((ord(s1[i]) - ord('A') + ord(s2[i]) - ord('A')) % 26 + ord('A'))
    return merge_message


if __name__ == '__main__':
    main()
