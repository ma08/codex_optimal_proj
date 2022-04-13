
import sys
import math

def main():
    message = sys.stdin.readline().strip()
    half1 = message[:len(message)//2]
    half2 = message[len(message)//2:]
    rotate1 = rotate_encrypt(half1)
    rotate2 = rotate_encrypt(half2)
    merge = merge_encrypt(rotate1, rotate2, len(message)//2)
    print(merge)
    print(merge_decrypt(merge, len(message)//2))

def rotate_encrypt(s):
    rotate = 0
    for i in range(len(s)):
        rotate += ord(s[i]) - ord('A')
    rotate = rotate % 26
    rotate_message = ''
    for i in range(len(s)):
        rotate_message += chr((ord(s[i]) - ord('A') + rotate) % 26 + ord('A'))
    return rotate_message

def merge_encrypt(s1, s2, length):
    merge_message = ''
    for i in range(length):
        merge_message += chr((ord(s1[i]) - ord('A') + ord(s2[i]) - ord('A')) % 26 + ord('A'))
    return merge_message

def merge_decrypt(s, length):
    merge_message = ''
    for i in range(length):
        merge_message += chr((ord(s[i]) - ord('A') - ord(s[i-1]) - ord('A')) % 26 + ord('A'))
    return merge_message

if __name__ == '__main__':
    main()
