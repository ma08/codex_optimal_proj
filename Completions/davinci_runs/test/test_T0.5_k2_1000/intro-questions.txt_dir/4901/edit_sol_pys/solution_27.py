
import sys

def main():
    message = sys.stdin.readline().strip()
    half1 = message[:len(message)//2]
    half2 = message[len(message)//2:]
    rotate1 = rotate(half1, half2)
    rotate2 = rotate(half2, half1)
    merge = merge(rotate1, rotate2, half1, half2)

    print(merge)

def rotate(s1, s2):
    rotate = 0
    for i in range(len(s1)):
        rotate += ord(s1[i]) - ord('A')
    rotate = rotate % 26
    rotate_message = ''
    for i in range(len(s1)):
        rotate_message += chr((ord(s1[i]) - ord('A') + rotate) % 26 + ord('A'))
    return rotate_message



def merge(s1, s2, s3, s4):
    merge_message = ''
    for i in range(len(s3)):
        merge_message += chr((ord(s1[i]) - ord('A') + ord(s2[i]) - ord('A')) % 26 + ord('A') + ord(s3[i]) - ord('A') + ord(s4[i]) - ord('A'))
    return merge_message


if __name__ == '__main__':
    main()
